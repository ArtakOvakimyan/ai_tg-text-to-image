import os
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from dotenv import load_dotenv

from handler.process_prompt import process_prompt

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, process_prompt))
    app.run_polling()
