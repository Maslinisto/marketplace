from fastapi import FastAPI
from app.routers import router as router_test
from app.database import engine, Base
#import app.models  # Импортирует все модели через __init__.py

app = FastAPI()

app.include_router(router_test)

# Создание всех таблиц
#Base.metadata.create_all(bind=engine) #при вкл приложения создадутся таблицы и в timestamp внесутся даты создания
