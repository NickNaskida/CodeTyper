import os

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class BaseSettings:
    SECRET_KEY = "SECRET_KEY"
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CODEMIRROR_LANGUAGES = ['python', 'javascript', 'go']
    CODEMIRROR_THEME = 'the-matrix'


class DevSettings(BaseSettings):
    DEBUG = True


settings = DevSettings()
