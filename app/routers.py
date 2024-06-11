from fastapi import APIRouter, HTTPException
from app.models.categories import Categories
from app.models.users import Users
from app.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

router=APIRouter(
    prefix='/test',
    tags=['Тест']
)

class UpdatePasswordRequest(BaseModel):
    new_password: str

@router.get("/add_user")
def add_user(db: Session = Depends(get_db)):
        new_user = Users(
            email='ddd@test.com',
            phone_number='8911111111',
            hashed_password='dsdsds'
        )
        db.add(new_user)
    
        # Сохранение изменений
        db.commit()
        
        # Обновление сессии для получения данных о новом пользователе (например, его ID)
        db.refresh(new_user)
        
        return {"message": "User added successfully", "user_id": new_user.id}

@router.get("/add_fav_prod")
def add_fav_prod(db: Session = Depends(get_db)):
        item = db.query(Categories.name).first()
        return item

@router.post("/update_password/{user_id}")
def update_password(user_id: int, request: UpdatePasswordRequest, db: Session = Depends(get_db)):
    # Поиск пользователя по id
    user = db.query(Users).filter(Users.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Обновление пароля пользователя
    user.hashed_password = request.new_password
    # Сохранение изменений
    db.commit()
    
    return {"message": "Password updated successfully"}