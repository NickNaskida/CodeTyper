from flask import Flask

from src.db import db
from src.config import settings
from src.modules import blueprints
from src.extensions import extensions, extensions_with_db


def import_models() -> None:
    """
    Import all models from src/models.

    :return: None
    """
    from src.models.snippet import SnippetModel


def register_extensions(app: Flask) -> None:
    """
    Register Flask extensions.

    :param app: Flask application instance
    :return: None
    """
    for extension in extensions:
        extension.init_app(app=app)

    for extension in extensions_with_db:
        extension.init_app(app=app, db=db)


def register_blueprints(app: Flask) -> None:
    """
    Method to register list of blueprints to the app.

    :param app: Flask application
    :return: None
    """
    if not blueprints and app.get("CHECK_FOR_BLUEPRINTS") is True:
        message = "The list of blueprints is empty. App won't have any blueprints."
        app.logger.warning(message)
    else:
        for blueprint in blueprints:
            app.register_blueprint(blueprint)


def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object(settings)

    import_models()

    register_extensions(app)
    register_blueprints(app)

    return app
