from app.configuration.server import Server
from fastapi import FastAPI


def create_app(_=None) -> FastAPI:

    app = FastAPI()

    return Server(app).get_app()
