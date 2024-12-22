import io
from PIL import Image


def bytes_to_image(image_bytes: bytes) -> io.BytesIO:
    image = Image.open(io.BytesIO(image_bytes))
    image_buffer = io.BytesIO()
    image.save(image_buffer, format='JPEG')
    image_buffer.seek(0)
    return image_buffer
