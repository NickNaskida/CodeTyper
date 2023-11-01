import os
import secrets

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class BaseSettings:
    SECRET_KEY = secrets.token_urlsafe(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevSettings(BaseSettings):
    DEBUG = True


settings = DevSettings()
