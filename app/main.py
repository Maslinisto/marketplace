from fastapi import FastAPI
from app.database import Author
from app.db_operations import session
from app.routers import router as router_test

app = FastAPI()

app.include_router(router_test)