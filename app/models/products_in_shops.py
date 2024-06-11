from typing import Optional
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.shops import Shops
from app.models.products import Products
class ProductsInShop(Base):
    __tablename__ = "products_in_shop"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(Integer, ForeignKey("shops.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), nullable=False)
    quantity: Mapped[float] = mapped_column(DECIMAL(10, 3), nullable=False, default=0)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False, default=0)
    discount: Mapped[Optional[float]] = mapped_column(DECIMAL, default=0)

    shop: Mapped["Shops"] = relationship(back_populates="products_in_shop")
    product: Mapped["Products"] = relationship(back_populates="products_in_shop")

    __table_args__ = (
        Index('idx_shop_product', 'shop_id', 'product_id', unique=True),
    )