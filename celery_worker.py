from celery import Celery

app = Celery("worker", broker="redis://localhost:8001/0")

@app.task
def process_image(message):
    # Здесь вы вызываете внешнее API для обработки изображения
    # Например, используя model.execute
    from model.model import Model
    model = Model()
    image_buffer = model.execute(message)
    return image_buffer
