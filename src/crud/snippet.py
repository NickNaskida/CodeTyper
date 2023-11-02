from src.crud.base import CRUDBase
from src.models.snippet import SnippetModel


class CRUDSnippet(CRUDBase[SnippetModel]):
    pass


snippet = CRUDSnippet(SnippetModel)

