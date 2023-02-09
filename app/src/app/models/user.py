from sqlalchemy.orm import declarative_base

from typing import Optional
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()

class User(Base):
     __tablename__ = "user_account"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str] = mapped_column(String(30))
     fullname: Mapped[Optional[str]]

     def __repr__(self) -> str:
         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
     __tablename__ = "user_address"

     id: Mapped[int] = mapped_column(primary_key=True)
     postcode: Mapped[str] = mapped_column(String(30))
     address: Mapped[Optional[str]]
     key: Mapped[str] = mapped_column(String(100))
     value: Mapped[int] = mapped_column(Integer)
     def __repr__(self) -> str:
         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
