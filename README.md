# Translate Feature

Simple Python Telethon Bot To Translate Messages Using googletrans Module.

## Features
- Translate messages into any language using the `/trn` command.
- List all supported languages with the `/languages` command.

## How to Use?

```bash
git clone https://github.com/iAayco/Translate
cd Translate
python bot.py
```

### Bot Commands
1. **/start**:
   - Displays a welcome message and instructions.
2. **/trn <language_code> <text>**:
   - Translates the given `<text>` into the specified `<language_code>`. Example: `/trn ar Hello`.
3. **/languages**:
   - Displays a list of all supported languages and their codes.

## Requirements

```bash
pip install -r requirements.txt
```

## Example Usage
1. Start the bot with `/start`.
2. Run `/languages` to see a list of supported languages.
3. Use `/trn` to translate messages:
   - Example: `/trn es Hello` will translate "Hello" to Spanish.
