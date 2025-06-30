from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from .base import Base

class User(Base):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(String(20))