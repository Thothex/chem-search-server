from app.api.routes import users
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
