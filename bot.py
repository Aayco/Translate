#Translation Bot Usig Telethon And Google Translate Module
from os import system
#Try To Import Modules
try:
    from telethon import TelegramClient, events
    from googletrans import Translator
except ImportError:
    #Install Modules If Not Installed
    system('pip install telethon googletrans==4.0.0-rc1')

#Some Cute Vars
translator = Translator()
#Your Api Id    
api_id = ''
#Your Api Hash
api_hash = ''
#Let's Start The Client 
bot = TelegramClient('bot', api_id, api_hash).start(bot_token='Your Bot Token')

#/start Command Handler
@bot.on(events.NewMessage(pattern='/start'))
async def welcome(event):
    #Cute Start Message
    start_message = (
        "👋 Hello there!\n\n"
        "Welcome to **My Translate Bot** 🤖.\n\n"
        "✨ Here are some things I can do:\n"
        "- Translate your messages into any language\n"
        "Type `/trn <language that you need to translate to> <your msg that you want to be translated>` to start using the bot."
        "ex: /trn ar Hello"
    )
    #Reply With Start Message If Someone Send /start
    await event.reply(start_message)

#/trn command Handler    
@bot.on(events.NewMessage(pattern=r'^/trn (.+) (.+)'))
async def translate(event):
    #Get The Lang You Need To Translate To From Message
    lang = event.pattern_match.group(1)
    try:
        #Get The Message You Need To Translate From Message
        msg = event.pattern_match.group(2)
        #If Message Found
        if msg:
            #Get Original Message Lang
            detected_language = translator.detect(msg).lang
            #Translate User Message From Original Lang To Inputed Lang
            translated_text = translator.translate(msg, src=detected_language, dest=lang)
            #Reply With Translated Message And Translate Info
            await event.reply(f'translated from {detected_language} to {lang}\n{translated_text.text}')
    except Exception as e:
        #Reply With Error If Happend
        await event.reply(str(e))

#Make Sure To Keep Bot Running If Not Disconnected        
bot.run_until_disconnected()
