from datetime import datetime

from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from db.base_class import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer)

    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    creation_date: Mapped[datetime] = mapped_column(DateTime, default=func.now())
