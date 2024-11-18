from telegram import Update
from telegram.ext import ContextTypes
from model.cv_model import CvModel
import io


async def process_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.photo:
        photo = update.message.photo[0]
        file_id = photo.file_id
        file = await context.bot.get_file(file_id)

        file_stream = io.BytesIO()


        await file.download_to_memory(out=file_stream)

        file_stream.seek(0)

        model = CvModel()
        await update.message.reply_text(model.process(file_stream))
        file_stream.close()