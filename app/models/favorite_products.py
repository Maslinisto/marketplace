from sqlalchemy import Integer, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.timestamp import TimestampMixin

class FavoriteProducts(TimestampMixin, Base):
    __tablename__ = "favorite_products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)

    user: Mapped["Users"] = relationship(back_populates="favorite_products")
    product: Mapped["Products"] = relationship(back_populates="favorite_products")
    __table_args__ = (
        Index('idx_user_fav_product', 'user_id', 'product_id', unique=True),
    )