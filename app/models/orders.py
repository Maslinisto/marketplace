from typing import TYPE_CHECKING, Optional
from sqlalchemy import Integer, String, DECIMAL, ForeignKey, JSON, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from models.users import Users
    
class Orders(Base):
    __tablename__ = "orders"
    
    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    order_date: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    ordered_items: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False, default="В сборке")
    total_amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    shipping_address: Mapped[str] = mapped_column(String, nullable=False)
    payment_method: Mapped[str] = mapped_column(String, nullable=False)
    payment_status: Mapped[str] = mapped_column(String, nullable=False, default="Не оплачен")
    shipping_method: Mapped[str] = mapped_column(String, nullable=False)
    shipping_cost: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False, default=0.00)
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user: Mapped["Users"] = relationship(back_populates="order")