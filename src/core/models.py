from typing import Optional

from core.db import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Programm(Base):
    __tablename__ = 'programms'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
