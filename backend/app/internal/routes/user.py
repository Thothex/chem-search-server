from fastapi import APIRouter, Body

router = APIRouter(prefix="/api/v1")


@router.get("/hello-world")
def set_user():

    return {"hello": "world"}
