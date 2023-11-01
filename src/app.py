from flask import Flask

from src.db import db
from src.config import settings
from src.extensions import extensions, extensions_with_db


def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object(settings)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_extensions(app) -> None:
    """
    Register Flask extensions.

    :param app: Flask application instance
    :return: None
    """
    for extension in extensions:
        extension.init_app(app=app)

    for extension in extensions_with_db:
        extension.init_app(app=app, db=db)


def register_blueprints(app) -> None:
    pass

