from fastapi import FastAPI
from app.routers import router as router_test

app = FastAPI()

app.include_router(router_test)