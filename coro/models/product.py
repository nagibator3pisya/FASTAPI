from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column

from .base import Base

class Product(Base):
    __tablename__ = 'product'
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(50))
    price: Mapped[int] = mapped_column(Integer())