from flask_migrate import Migrate
from flask_codemirror import CodeMirror

from src.db import db


migrate = Migrate()
codemirror = CodeMirror()


extensions = [db, codemirror]
extensions_with_db = [migrate]
