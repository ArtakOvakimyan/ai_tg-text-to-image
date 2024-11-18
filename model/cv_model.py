from transformers import pipeline
from PIL import Image


class CvModel:
    def __init__(self):
        self.pipe = pipeline("image-classification", model="Organika/sdxl-detector")

    def process(self, file):
        image = Image.open(file)
        return self.pipe(image)
