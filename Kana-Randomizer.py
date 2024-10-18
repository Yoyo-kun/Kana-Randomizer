import tkinter as tk
from tkinter import messagebox
import random
import pygame
import os
import sys

# 获取资源路径
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path

# 初始化 pygame
pygame.mixer.init()

# 平假名与罗马音和片假名的映射
kana_dict = [
    ['あ', 'a', 'ア'], ['い', 'i', 'イ'], ['う', 'u', 'ウ'],
    ['え', 'e', 'エ'], ['お', 'o', 'オ'], ['か', 'ka', 'カ'],
    ['き', 'ki', 'キ'], ['く', 'ku', 'ク'], ['け', 'ke', 'ケ'],
    ['こ', 'ko', 'コ'], ['さ', 'sa', 'サ'], ['し', 'shi', 'シ'],
    ['す', 'su', 'ス'], ['せ', 'se', 'セ'], ['そ', 'so', 'ソ'],
    ['た', 'ta', 'タ'], ['ち', 'chi', 'チ'], ['つ', 'tsu', 'ツ'],
    ['て', 'te', 'テ'], ['と', 'to', 'ト'], ['な', 'na', 'ナ'],
    ['に', 'ni', 'ニ'], ['ぬ', 'nu', 'ヌ'], ['ね', 'ne', 'ネ'],
    ['の', 'no', 'ノ'], ['は', 'ha', 'ハ'], ['ひ', 'hi', 'ヒ'],
    ['ふ', 'fu', 'フ'], ['へ', 'he', 'ヘ'], ['ほ', 'ho', 'ホ'],
    ['ま', 'ma', 'マ'], ['み', 'mi', 'ミ'], ['む', 'mu', 'ム'],
    ['め', 'me', 'メ'], ['も', 'mo', 'モ'], ['や', 'ya', 'ヤ'],
    ['ゆ', 'yu', 'ユ'], ['よ', 'yo', 'ヨ'], ['ら', 'ra', 'ラ'],
    ['り', 'ri', 'リ'], ['る', 'ru', 'ル'], ['れ', 're', 'レ'],
    ['ろ', 'ro', 'ロ'], ['わ', 'wa', 'ワ'], ['を', 'wo', 'ヲ'],
    ['ん', 'n', 'ン']
    # # 拗音
    # ['きゃ', 'kya', 'キャ'], ['きゅ', 'kyu', 'キュ'], ['きょ', 'kyo', 'キョ'],
    # ['しゃ', 'sha', 'シャ'], ['しゅ', 'shu', 'シュ'], ['しょ', 'sho', 'ショ'],
    # ['ちゃ', 'cha', 'チャ'], ['ちゅ', 'chu', 'チュ'], ['ちょ', 'cho', 'チョ'],
    # ['にゃ', 'nya', 'ニャ'], ['にゅ', 'nyu', 'ニュ'], ['にょ', 'nyo', 'ニョ'],
    # ['ひゃ', 'hya', 'ヒャ'], ['ひゅ', 'hyu', 'ヒュ'], ['ひょ', 'hyo', 'ヒョ'],
    # ['みゃ', 'mya', 'ミャ'], ['みゅ', 'myu', 'ミュ'], ['みょ', 'myo', 'ミョ'],
    # ['りゃ', 'rya', 'リャ'], ['りゅ', 'ryu', 'リュ'], ['りょ', 'ryo', 'リョ']
]

# 生成多个随机排列的函数
def generate_multiple_random_groups():
    try:
        quantity = int(quantity_entry.get())
        if quantity < 1:
            raise ValueError
    except ValueError:
        quantity = 80  # 默认数量

    input_text = entry.get().strip()

    # 默认的平假名和片假名
    default_kana ='''
    あ ア い イ う ウ え エ お オ 
    か カ き キ く ク け ケ こ コ 
    さ サ し シ す ス せ セ そ ソ 
    た タ ち チ つ ツ て テ と ト 
    な ナ に ニ ぬ ヌ ね ネ の ノ 
    は ハ ひ ヒ ふ フ へ ヘ ほ ホ 
    ま マ み ミ む ム め メ も モ 
    や ヤ ゆ ユ よ ヨ 
    ら ラ り リ る ル れ レ ろ ロ 
    わ ワ を ヲ 
    ん ン
    '''

    if not input_text:
        input_text = default_kana  # 如果输入为空，使用默认的假名

    groups = [kana for kana in kana_dict if kana[0] in input_text or kana[2] in input_text]

    if not groups:
        messagebox.showerror("错误", "没有匹配的假名")
        return

    # 确保每个元素至少出现一次，然后随机补充
    selected_groups = random.choices(groups, k=quantity)

    for widget in result_frame.winfo_children():
        widget.destroy()

    # 生成指定数量的按钮，每行十个
    for idx, group in enumerate(selected_groups):
        # 从选定的组中随机选择平假名或片假名作为初始状态
        if group[0] in input_text and group[2] in input_text:
            text, bg_color = random.choice([(group[0], 'lightblue'), (group[2], 'lightgreen')])
            flag = -1 if text == group[0] else 1
        elif group[0] in input_text:
            text, bg_color = group[0], 'lightblue'
            flag = -1
        else:
            text, bg_color = group[2], 'lightgreen'
            flag = 1

        button = tk.Button(result_frame, text=text, bg=bg_color, font=("Arial", 14, "bold"), width=10, height=2)
        button.flag = flag  # 设置状态
        button.config(command=lambda btn=button, g=group: toggle_kana(btn, g))
        button.grid(row=idx // 10, column=idx % 10, padx=5, pady=5)

# 定义音频播放函数
def play_sound(sound_file):
    sound_file = resource_path(sound_file)
    pygame.mixer.Sound(sound_file).play()

# 音频文件映射字典
audio_dict = {
    'あ': 'a.mp3', 'い': 'i.mp3', 'う': 'u.mp3', 'え': 'e.mp3', 'お': 'o.mp3',
    'か': 'ka.mp3', 'き': 'ki.mp3', 'く': 'ku.mp3', 'け': 'ke.mp3', 'こ': 'ko.mp3',
    'さ': 'sa.mp3', 'し': 'shi.mp3', 'す': 'su.mp3', 'せ': 'se.mp3', 'そ': 'so.mp3',
    'た': 'ta.mp3', 'ち': 'chi.mp3', 'つ': 'tsu.mp3', 'て': 'te.mp3', 'と': 'to.mp3',
    'な': 'na.mp3', 'に': 'ni.mp3', 'ぬ': 'nu.mp3', 'ね': 'ne.mp3', 'の': 'no.mp3',
    'は': 'ha.mp3', 'ひ': 'hi.mp3', 'ふ': 'fu.mp3', 'へ': 'he.mp3', 'ほ': 'ho.mp3',
    'ま': 'ma.mp3', 'み': 'mi.mp3', 'む': 'mu.mp3', 'め': 'me.mp3', 'も': 'mo.mp3',
    'や': 'ya.mp3', 'ゆ': 'yu.mp3', 'よ': 'yo.mp3',
    'ら': 'ra.mp3', 'り': 'ri.mp3', 'る': 'ru.mp3', 'れ': 're.mp3', 'ろ': 'ro.mp3',
    'わ': 'wa.mp3', 'を': 'wo.mp3', 'ん': 'n.mp3',
    # 片假名映射
    'ア': 'a.mp3', 'イ': 'i.mp3', 'ウ': 'u.mp3', 'エ': 'e.mp3', 'オ': 'o.mp3',
    'カ': 'ka.mp3', 'キ': 'ki.mp3', 'ク': 'ku.mp3', 'ケ': 'ke.mp3', 'コ': 'ko.mp3',
    'サ': 'sa.mp3', 'シ': 'shi.mp3', 'ス': 'su.mp3', 'セ': 'se.mp3', 'ソ': 'so.mp3',
    'タ': 'ta.mp3', 'チ': 'chi.mp3', 'ツ': 'tsu.mp3', 'テ': 'te.mp3', 'ト': 'to.mp3',
    'ナ': 'na.mp3', 'ニ': 'ni.mp3', 'ヌ': 'nu.mp3', 'ネ': 'ne.mp3', 'ノ': 'no.mp3',
    'ハ': 'ha.mp3', 'ヒ': 'hi.mp3', 'フ': 'fu.mp3', 'ヘ': 'he.mp3', 'ホ': 'ho.mp3',
    'マ': 'ma.mp3', 'ミ': 'mi.mp3', 'ム': 'mu.mp3', 'メ': 'me.mp3', 'モ': 'mo.mp3',
    'ヤ': 'ya.mp3', 'ユ': 'yu.mp3', 'ヨ': 'yo.mp3',
    'ラ': 'ra.mp3', 'リ': 'ri.mp3', 'ル': 'ru.mp3', 'レ': 're.mp3', 'ロ': 'ro.mp3',
    'ワ': 'wa.mp3', 'ヲ': 'wo.mp3', 'ン': 'n.mp3',
    # 拗音    这部分缺少音频文件，请自行添加到 Kana_basic_sounds 中
    # # 平假名对应
    # 'きゃ': 'kya.mp3', 'きゅ': 'kyu.mp3', 'きょ': 'kyo.mp3',
    # 'しゃ': 'sha.mp3', 'しゅ': 'shu.mp3', 'しょ': 'sho.mp3',
    # 'ちゃ': 'cha.mp3', 'ちゅ': 'chu.mp3', 'ちょ': 'cho.mp3',
    # 'にゃ': 'nya.mp3', 'にゅ': 'nyu.mp3', 'にょ': 'nyo.mp3',
    # 'ひゃ': 'hya.mp3', 'ひゅ': 'hyu.mp3', 'ひょ': 'hyo.mp3',
    # 'みゃ': 'mya.mp3', 'みゅ': 'myu.mp3', 'みょ': 'myo.mp3',
    # 'りゃ': 'rya.mp3', 'りゅ': 'ryu.mp3', 'りょ': 'ryo.mp3',
    # # 片假名对应
    # 'キャ': 'kya.mp3', 'キュ': 'kyu.mp3', 'キョ': 'kyo.mp3',
    # 'シャ': 'sha.mp3', 'シュ': 'shu.mp3', 'ショ': 'sho.mp3',
    # 'チャ': 'cha.mp3', 'チュ': 'chu.mp3', 'チョ': 'cho.mp3',
    # 'ニャ': 'nya.mp3', 'ニュ': 'nyu.mp3', 'ニョ': 'nyo.mp3',
    # 'ヒャ': 'hya.mp3', 'ヒュ': 'hyu.mp3', 'ヒョ': 'hyo.mp3',
    # 'ミャ': 'mya.mp3', 'ミュ': 'myu.mp3', 'ミョ': 'myo.mp3',
    # 'リャ': 'rya.mp3', 'リュ': 'ryu.mp3', 'リョ': 'ryo.mp3'
}

# 点击触发状态变换
def toggle_kana(button, group):
    sound_file = "Kana_basic_sounds/"  # 相对路径
    if button.flag == -1:  # 平假名状态
        button.config(text=group[1], bg='lightcoral')  # 显示罗马音并变为红色
        button.flag = 0  # 状态变为0
        # 播放对应平假名的音频
        play_sound(sound_file + audio_dict.get(group[0], "default.mp3"))
    elif button.flag == 0:  # 罗马音状态
        button.flag = random.choice([-1, 1])  # 随机选择下一个状态
        if button.flag == -1:
            button.config(text=group[0], bg='lightblue')  # 回到平假名
            # 播放对应平假名的音频
            play_sound(sound_file + audio_dict.get(group[0], "default.mp3"))
        else:
            button.config(text=group[2], bg='lightgreen')  # 显示片假名并变为绿色
            # 播放对应片假名的音频
            play_sound(sound_file + audio_dict.get(group[2], "default.mp3"))
    elif button.flag == 1:  # 片假名状态
        button.config(text=group[1], bg='lightcoral')  # 显示罗马音并变为红色
        button.flag = 0  # 状态变为0
        # 播放对应片假名的音频
        play_sound(sound_file + audio_dict.get(group[2], "default.mp3"))


root = tk.Tk()
root.title("随机分组生成器")
root.state('zoomed')

label1 = tk.Label(root, text="请输入你的文本（默认为全体假名）", font=("Arial", 16, "bold"))
label1.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 14))
entry.pack(pady=5)

quantity_label = tk.Label(root, text="请输入生成数量（默认80）", font=("Arial", 16, "bold"))
quantity_label.pack(pady=10)

quantity_entry = tk.Entry(root, width=5, font=("Arial", 14))
quantity_entry.pack(pady=5)
quantity_entry.insert(0, '80')  # 默认值

generate_button = tk.Button(root, text="生成", font=("Arial", 14, "bold"), command=generate_multiple_random_groups)
generate_button.pack(pady=20)

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

root.mainloop()