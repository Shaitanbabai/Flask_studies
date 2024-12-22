import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    UPLOAD_FOLDER = 'static/uploads'
    JSON_DATA_FILE = 'data/users.json'