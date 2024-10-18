# 随机假名生成器

这是一个简单的 Tkinter 应用程序，用于根据用户输入的平假名或片假名生成随机按钮。每个按钮代表一个假名，可以通过点击按钮来查看其对应的罗马音或其他假名形式。

## 功能

- 输入平假名或片假名，生成相应的按钮。
- 按钮状态可在平假名、罗马音和片假名之间切换。
- 用户可以指定生成的按钮数量（默认80）。
- 每个假名至少出现一次，并且可以重复生成。

## 安装和使用

### 1. 安装依赖

在命令行中使用以下命令安装所需的 Python 库：

```bash
pip install -r requirements.txt
```

### 2. 下载并生成 .exe 文件

要将 Python 应用程序打包为 `.exe` 文件，你可以使用 `PyInstaller` 工具。请按照以下步骤操作：

1.  **安装 PyInstaller**

    如果尚未安装 `PyInstaller`，请在命令行中运行以下命令：

    ```bash
    pip install pyinstaller
    ```
    
2.  **打包应用程序**

    在命令行中导航到包含 `main.py` 的项目目录，然后运行以下命令：

    ```bash
    pyinstaller --onefile --windowed Kana-Randomizer.py
    ```
    
    -   `--onefile` 选项将所有文件打包成一个单独的 `.exe` 文件。
    -   `--windowed` 选项会隐藏命令行窗口。
    
3.  **查找生成的 .exe 文件**

    打包完成后，生成的 `.exe` 文件将位于 `dist` 文件夹中。你可以在该文件夹中找到并运行它。

