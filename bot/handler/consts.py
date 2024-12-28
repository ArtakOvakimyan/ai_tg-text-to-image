from dotenv import load_dotenv
import os

load_dotenv()
MODEL_ADDRESS = os.getenv('MODEL_ADDRESS')

API_URL = MODEL_ADDRESS