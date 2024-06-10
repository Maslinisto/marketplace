from typing import Optional
from sqlalchemy import Boolean, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Products(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)
    image: Mapped[Optional[str]] = mapped_column(String)
    details: Mapped[Optional[str]] = mapped_column(String)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    available: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    category: Mapped["Categories"] = relationship(back_populates="products")
    carts: Mapped[list["Carts"]] = relationship("Carts", back_populates="product")
    favorite_products: Mapped[list["FavoriteProducts"]] = relationship(back_populates="product")
    reviews: Mapped[list["Reviews"]] = relationship(back_populates="product")
    products_in_shop: Mapped[list["ProductsInShop"]] = relationship(back_populates="product")