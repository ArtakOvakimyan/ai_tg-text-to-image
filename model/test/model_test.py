import pytest
from fastapi.testclient import TestClient
from model.model_api_wrapped import app
import time

client = TestClient(app)


# Функция для повторной отправки запросов при ошибке 500
def make_request_with_retries(endpoint, payload, retries=5, delay=20):
    for attempt in range(retries):
        response = client.post(endpoint, json=payload)
        if response.status_code != 500:
            return response
        if attempt < retries - 1:
            time.sleep(delay)
    pytest.fail("Ошибка 500: сервер может быть перегружен после всех попыток.")


# 1. Интеграционные тесты
def test_model_loading_and_prediction():
    response = make_request_with_retries("/process", {"message": "test input"})
    assert response.status_code == 200, "API не вернул успешный статус."
    assert response.headers["content-type"] == "image/png", "Ответ не является изображением."
    assert len(response.content) > 0, "Ответ пустой."


# 2. Регрессионные тесты
@pytest.mark.parametrize("input_text", [
    "test input 1",
    "test input 2",
    "another test input",
])
def test_regression(input_text):
    response = make_request_with_retries("/process", {"message": input_text})
    assert response.status_code == 200, "API не вернул успешный статус."
    assert response.headers["content-type"] == "image/png", "Ответ не является изображением."
    assert len(response.content) > 0, "Ответ пустой."


# 3. Приемочные тесты
def test_acceptance():
    response = make_request_with_retries("/process", {"message": "valid input"})
    assert response.status_code == 200, "API не принимает корректные входные данные."
    assert response.headers["content-type"] == "image/png", "Ответ не является изображением."

    invalid_response = make_request_with_retries("/process", {"invalid_key": "invalid input"})
    assert invalid_response.status_code == 422, "API не возвращает ошибку для некорректного ввода."

    empty_response = make_request_with_retries("/process", {"message": ""})
    assert empty_response.status_code == 200, "API возвращает ошибку для пустого ввода."


# 4. Нагрузочные тесты
def test_load():
    # Кеширование и задержку запросов реализует API Telegram
    responses = []
    for _ in range(10):
        response = make_request_with_retries("/process", {"message": "test input under load"})
        responses.append(response)

    for response in responses:
        assert response.status_code == 200, "API не выдерживает нагрузку."
        assert response.headers["content-type"] == "image/png", "Ответ не является изображением."
        assert len(response.content) > 0, "Ответ пустой под нагрузкой."


# 5. Параметризованные тесты
@pytest.mark.parametrize("input_text", [
    "simple test input",
    "input with special characters !@#$%^&*()",
    "input with numbers 1234567890",
    "",
    None
])
def test_prediction_with_various_inputs(input_text):
    response = make_request_with_retries("/process", {"message": input_text})
    if input_text is None:
        assert response.status_code == 422, "API не возвращает ошибку для некорректного ввода."
    else:
        assert response.status_code == 200, "API не обрабатывает корректные данные."
        assert response.headers["content-type"] == "image/png", "Ответ не является изображением."
        assert len(response.content) > 0, "Ответ пустой для входа: {input_text}"

if __name__ == "__main__":
    pytest.main()