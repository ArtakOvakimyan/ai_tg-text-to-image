from telegram import Update
from telegram.ext import ContextTypes
from .consts import API_URL
import requests


async def process_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    if not message:
        return
    init_msg = await update.message.reply_text("Generating response...")

    try:
        response = requests.post(API_URL, json={"message": message})
        if response.status_code != 200:
            raise Exception(response.json())
        image_data = response.content
        await update.message.chat.send_photo(photo=image_data)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")
    finally:
        await init_msg.delete()
