from src.db import db, Column
from src.models.base import BaseModel


class SnippetModel(BaseModel):
    """Code snippet model."""

    __tablename__ = 'code_snippets'

    code = Column(db.Text())
