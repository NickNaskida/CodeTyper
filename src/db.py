from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.models.base import BaseModel


db = SQLAlchemy(model_class=BaseModel)

