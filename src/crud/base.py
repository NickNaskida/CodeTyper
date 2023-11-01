from typing import Any, List, Optional, Type, TypeVar, Generic

from sqlalchemy import exc, func
from sqlalchemy import select

from src.db import db
from src.models.base import BaseModel


ModelType = TypeVar("ModelType", bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]) -> None:
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        :param model: A SQLAlchemy model class
        """
        self.model = model
        self.db = db

    def get_db(self):
        return self.db

    def get_db_session(self):
        return self.db.session

    def create(
        self,
        *,
        obj_new: ModelType,
    ) -> ModelType:
        db_session = self.get_db_session()

        try:
            db_session.add(obj_new)
            db_session.commit()
        except Exception as e:
            db_session.rollback()
            raise Exception(f"Integrity Error {e}")

        db_session.refresh(obj_new)

        return obj_new

    def get(self, _id: Any) -> Optional[ModelType]:
        db_session = self.get_db_session()
        query = select(self.model).where(self.model.id == _id)
        response = db_session.execute(query)
        return response.scalar_one_or_none()

    def get_multi(
        self,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> List[ModelType]:
        db_session = self.get_db_session()
        query = select(self.model).offset(skip).limit(limit).order_by(self.model.id)
        response = db_session.execute(query)
        return response.scalars()

    def get_count(self) -> ModelType | None:
        db_session = self.get_db_session()
        response = db_session.execute(
            select(func.count()).select_from(select(self.model).subquery())
        )
        return response.scalar_one()

    def update(
        self,
        *,
        obj_current: ModelType,
        **kwargs: Any,
    ) -> ModelType:
        db_session = self.get_db_session()

        for key, value in kwargs.items():
            setattr(obj_current, key, value)

        db_session.add(obj_current)
        db_session.commit()
        db_session.refresh(obj_current)

        return obj_current

    def remove(self, *, _id: int) -> ModelType:
        db_session = self.get_db_session()
        query = select(self.model).where(self.model.id == _id)
        response = db_session.execute(query)
        obj = response.scalar_one()
        db_session.delete(obj)
        db_session.commit()

        return obj
