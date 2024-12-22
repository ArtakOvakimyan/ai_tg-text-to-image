import os
import requests
from .consts import HF_API_URL
from dotenv import load_dotenv

load_dotenv()


def get_image_from_hf_api(prompt: str) -> bytes:
    headers = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
    payload = {"inputs": prompt}
    response = requests.post(HF_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Ошибка API: {response.status_code}, {response.text}")
