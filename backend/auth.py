from fastapi import APIRouter
from models import User

auth_router = APIRouter()

@auth_router.post("/signup")
async def register_user(user: User):
    return {"message": f"User {user.username} created!"}