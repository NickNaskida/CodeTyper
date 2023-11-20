from src.db import db, Column
from src.models.base import BaseModel


class SnippetModel(BaseModel):
    """Code snippet model."""

    __tablename__ = 'code_snippets'

    language = Column(db.String(50), nullable=False)
    code = Column(db.Text(), nullable=False)
