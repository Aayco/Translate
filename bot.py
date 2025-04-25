# Translation Bot Using Telethon And Google Translate Module
from telethon import TelegramClient, events
from googletrans import Translator, LANGUAGES

# Some Cute Vars
translator = Translator()
# Your Api Id    
api_id = ''
# Your Api Hash
api_hash = ''
# Let's Start The Client 
bot = TelegramClient('bot', api_id, api_hash).start(bot_token='Your Bot Token')

# /start Command Handler
@bot.on(events.NewMessage(pattern='/start'))
async def welcome(event):
    # Cute Start Message
    start_message = (
        "👋 Hello there!\n\n"
        "Welcome to **My Translate Bot** 🤖.\n\n"
        "✨ Here are some things I can do:\n"
        "- Translate your messages into any language\n"
        "Type `/trn <language that you need to translate to> <your msg that you want to be translated>` to start using the bot.\n"
        "ex: /trn ar Hello\n"
        "Type `/languages` to get a list of supported languages."
    )
    # Reply With Start Message If Someone Sends /start
    await event.reply(start_message)

# /languages Command Handler
@bot.on(events.NewMessage(pattern='/languages'))
async def list_languages(event):
    # Generate a list of supported languages
    languages = "\n".join([f"{code}: {name}" for code, name in LANGUAGES.items()])
    message = (
        "🌍 **Supported Languages:**\n\n"
        f"{languages}\n\n"
        "Use the language code with `/trn` command to translate your messages."
    )
    # Reply with the list of supported languages
    await event.reply(message)

# /trn command Handler    
@bot.on(events.NewMessage(pattern=r'^/trn (.+) (.+)'))
async def translate(event):
    # Get The Lang You Need To Translate To From Message
    lang = event.pattern_match.group(1)
    try:
        # Get The Message You Need To Translate From Message
        msg = event.pattern_match.group(2)
        # If Message Found
        if msg:
            # Get Original Message Lang
            detected_language = translator.detect(msg).lang
            # Translate User Message From Original Lang To Inputed Lang
            translated_text = translator.translate(msg, src=detected_language, dest=lang)
            # Reply With Translated Message And Translate Info
            await event.reply(f"Translated from {detected_language} to {lang}:\n{translated_text.text}")
    except Exception as e:
        # Reply With Error If Happend
        await event.reply(f"❌ Error: {str(e)}")

# Make Sure To Keep Bot Running If Not Disconnected        
bot.run_until_disconnected()
