# daos/carts_dao.py
from sqlalchemy.orm import Session
from app.models.carts import Carts
from app.models.products import Products
from decimal import Decimal

class CartsDAO:
    @staticmethod
    def add_to_cart(user_id: int, product_id: int, quantity: float, db: Session):
        # Проверяем наличие продукта и его доступность
        product = db.query(Products).filter(Products.id == product_id, Products.available == True).first()
        if not product:
            raise ValueError("Product not found or not available")

        # Вычисляем стоимость позиции
        # Предположим, что цена продукта хранится в каком-то поле, например, product.price
        # Если у вас нет такого поля, нужно будет его добавить
        cost_of_position = 1000 * Decimal(quantity)
        
        # Проверяем, есть ли уже такая позиция в корзине
        cart_item = db.query(Carts).filter(Carts.user_id == user_id, Carts.product_id == product_id).first()
        
        if cart_item:
            # Обновляем количество и стоимость позиции
            cart_item.quantity = cart_item.quantity + quantity
            cart_item.cost_of_position = Decimal(cart_item.cost_of_position) + cost_of_position
        else:
            # Добавляем новую позицию в корзину
            new_cart_item = Carts(
                user_id=user_id,
                product_id=product_id,
                quantity=quantity,
                cost_of_position=float(cost_of_position)
            )
            db.add(new_cart_item)
        
        db.commit()
