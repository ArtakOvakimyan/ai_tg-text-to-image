import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

from handler.process_image import process_image

load_dotenv()
BOT_TOKEN = os.getenv('TOKEN')


if __name__ == '__main__':
  app = ApplicationBuilder().token(BOT_TOKEN).build()
  app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, process_image))
  app.run_polling()