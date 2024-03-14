from app.api.routes import auth, users
from fastapi import FastAPI

app = FastAPI()

app.include_router(users.router, prefix="/api/v1")
app.include_router(auth.router, prefix="/api/v1")
