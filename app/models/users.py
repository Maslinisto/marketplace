from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, Integer, Boolean, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import func
from app.database import Base
from datetime import datetime

if TYPE_CHECKING:
    from models.orders import Orders
    from models.carts import Carts
    from models.favorite_products import FavoriteProducts
    from models.reviews import Reviews
class Users(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String)
    phone_number: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    shipping_address: Mapped[Optional[str]] = mapped_column(String)
    role: Mapped[Optional[str]] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())

    carts: Mapped[list["Carts"]] = relationship(back_populates="user")
    orders: Mapped[List["Orders"]] = relationship(back_populates="user")
    favorite_products: Mapped[list["FavoriteProducts"]] = relationship(back_populates="user")
    #fav_prods: Mapped[list["FavProds"]] = relationship(back_populates="user")
    reviews: Mapped[list["Reviews"]] = relationship(back_populates="user")