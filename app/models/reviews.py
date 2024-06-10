from typing import Optional
from sqlalchemy import Integer, Text, TIMESTAMP, ForeignKey, func, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Reviews(Base):
    __tablename__ = "reviews"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[Optional[str]] = mapped_column(Text)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())

    user: Mapped["Users"] = relationship(back_populates="reviews")
    product: Mapped["Products"] = relationship(back_populates="reviews")

    __table_args__ = (
        Index('idx_user_product_reviews', 'user_id', 'product_id', unique=True),
    )