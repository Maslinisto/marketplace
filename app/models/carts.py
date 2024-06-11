from sqlalchemy import Integer, DECIMAL, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.timestamp import TimestampMixin

class Carts(TimestampMixin, Base):
    __tablename__ = "carts"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[float] = mapped_column(DECIMAL(10, 3), nullable=False)
    cost_of_position: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)

    user: Mapped["Users"] = relationship(back_populates="carts")
    product: Mapped["Products"] = relationship(back_populates="carts")

    __table_args__ = (
        Index('idx_user_product', 'user_id', 'product_id', unique=True),
    )