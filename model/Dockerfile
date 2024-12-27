FROM python:3.12-slim

WORKDIR /app

COPY ../model/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-m", "fastapi", "run", "model/model_api_wrapped.py", "--host", "0.0.0.0", "--port", "8000"]

