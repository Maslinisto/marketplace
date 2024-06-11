from sqlalchemy import Integer, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.users import Users
from app.models.products import Products
from app.timestamp import TimestampMixin
#модель чисто для тестов
class FavProds(TimestampMixin, Base):
    __tablename__ = "fav_prods"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("products.id"), primary_key=True, nullable=False)

    user: Mapped["Users"] = relationship(back_populates="fav_prods")
    product: Mapped["Products"] = relationship(back_populates="fav_prods")


