# Kana Randomizer

This is a simple Tkinter application that generates random buttons representing hiragana or katakana based on user input. Each button can be clicked to reveal its corresponding romaji or other kana forms.

## Features

- Input hiragana or katakana to generate corresponding buttons.
- Button states can toggle between hiragana, romaji, and katakana.
- Users can specify the number of buttons to generate (default: 80).
- Each kana appears at least once and can be generated multiple times.

## Installation and Usage

### 1. Install Dependencies

Use the following command in the command line to install the required Python libraries:

```bash
pip install -r requirements.txt
```

### 2. Download and Generate .exe File

To package the Python application as an `.exe` file, you can use the `PyInstaller` tool. Follow these steps:

1. **Install PyInstaller**

   If you haven't installed `PyInstaller`, run the following command in the command line:

   ```bash
   pip install pyinstaller
   ```

2. **Package the Application**

   Navigate to the project directory containing `main.py` and run the following command:

   ```bash
   pyinstaller --onefile --noconsole --add-data "Kana_basic_sounds;Kana_basic_sounds" --icon="NERV.ico" Kana-Randomizer.py
   ```

   - The `--onefile` option packages all files into a single `.exe` file.
   - The `--windowed` option hides the command line window.

3. **Locate the Generated .exe File**

   Once packaging is complete, the generated `.exe` file will be found in the `dist` folder. You can find and run it from there.