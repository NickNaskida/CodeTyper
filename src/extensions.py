from flask_migrate import Migrate

from src.db import db


migrate = Migrate()


extensions = [db]
extensions_with_db = [migrate]
