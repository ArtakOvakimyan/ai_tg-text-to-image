from .helper.bytes_to_image import bytes_to_image
from .helper.get_image import get_image_from_hf_api
import io


class Model:
    def execute(self, message):
        image_bytes = get_image_from_hf_api(message)
        image_buffer = bytes_to_image(image_bytes)
        if isinstance(image_buffer, io.BytesIO):
            image_buffer = image_buffer.getvalue()
        return image_buffer
