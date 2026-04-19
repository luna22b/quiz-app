from fastapi import APIRouter
from app.db.schemas.user import UserInCreate, UserInLogin
authRouter = APIRouter()

@authRouter.post("/login")
def login(loginDetails: UserInLogin):
    return {"data": "login"}

@authRouter.post("/signup") 
def signUp(signupDetails: UserInCreate):
    return {"data":"signed up"}