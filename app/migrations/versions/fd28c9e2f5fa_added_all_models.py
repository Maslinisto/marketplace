"""'added_all_models'

Revision ID: fd28c9e2f5fa
Revises: 
Create Date: 2024-06-10 14:34:42.041830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd28c9e2f5fa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_date', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('ordered_items', sa.JSON(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('total_amount', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('shipping_address', sa.String(), nullable=False),
    sa.Column('payment_method', sa.String(), nullable=False),
    sa.Column('payment_status', sa.String(), nullable=False),
    sa.Column('shipping_method', sa.String(), nullable=False),
    sa.Column('shipping_cost', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('carts',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('cost_of_position', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'product_id')
    )
    op.create_index('idx_user_product', 'carts', ['user_id', 'product_id'], unique=True)
    op.create_table('favorite_products',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'product_id')
    )
    op.create_index('idx_user_fav_product', 'favorite_products', ['user_id', 'product_id'], unique=True)
    op.create_table('products_in_shop',
    sa.Column('shop_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.DECIMAL(precision=10, scale=3), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('discount', sa.DECIMAL(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['shop_id'], ['shops.id'], ),
    sa.PrimaryKeyConstraint('shop_id', 'product_id')
    )
    op.create_index('idx_shop_product', 'products_in_shop', ['shop_id', 'product_id'], unique=True)
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_user_product_reviews', 'reviews', ['user_id', 'product_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_user_product_reviews', table_name='reviews')
    op.drop_table('reviews')
    op.drop_index('idx_shop_product', table_name='products_in_shop')
    op.drop_table('products_in_shop')
    op.drop_index('idx_user_fav_product', table_name='favorite_products')
    op.drop_table('favorite_products')
    op.drop_index('idx_user_product', table_name='carts')
    op.drop_table('carts')
    op.drop_table('orders')
    # ### end Alembic commands ###
