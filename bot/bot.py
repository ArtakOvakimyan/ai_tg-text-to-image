import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

if __name__ == '__main__':
    from handler.process_prompt import process_prompt
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, process_prompt))
    app.run_polling(allowed_updates=Update.ALL_TYPES)