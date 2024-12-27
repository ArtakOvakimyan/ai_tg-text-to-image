from fastapi import FastAPI, HTTPException
from io import BytesIO
from fastapi.responses import StreamingResponse
from .model import Model
from .types.MessageRequest import MessageRequest

app = FastAPI()
model = Model()


@app.post("/process")
def process_message(request: MessageRequest):
    try:
        image_buffer = model.execute(request.message)
        if not image_buffer:
            raise HTTPException(status_code=400, detail="Failed to process the message.")

        return StreamingResponse(
            BytesIO(image_buffer), media_type="image/png"
        )
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
