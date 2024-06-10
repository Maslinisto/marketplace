from fastapi import APIRouter
from app.models.users import Users
from app.models.favorite_products import FavoriteProducts
from app.database import sessionmaker

router=APIRouter(
    prefix='/test',
    tags=['Тест']
)

#@router.get("/")
#def read_root():
#    with sessionmaker() as session:
#        return (session.query(Author).all())

@router.get("/add_user")
def add_user():
    with sessionmaker() as session:
        new_user = Users(email = 'ddd@test.com', phone_number = '8911111111', hashed_password = 'dsdsds')
        session.add(new_user)
        session.commit()
        return new_user
    
@router.get("/add_fav_prod")
def add_fav_prod():
    with sessionmaker() as session:
        new_prod = FavoriteProducts(user_id = 1, product_id = 2)
        session.add(new_prod)
        session.commit()
        return new_prod
#query = update(Author).where(Author.id==1).values(last_name="daaaas")
#result = session.execute(query)