from typing import Optional, List
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from app.database import Base
from app.models.timestamp import TimestampMixin

class Categories(TimestampMixin, Base):
    __tablename__ = "categories"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("categories.id"))

    parent: Mapped[Optional["Categories"]] = relationship("Categories", remote_side=[id], back_populates="children")
    children: Mapped[List["Categories"]] = relationship("Categories", back_populates="parent")
    products: Mapped[list["Products"]] = relationship(back_populates="category")

