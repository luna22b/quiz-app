from fastapi import APIRouter, Depends
from app.db.schemas.user import UserInCreate, UserInLogin
from app.core.database import get_db
from sqlalchemy.orm import Session
from app.service.userService import UserService
authRouter = APIRouter()

@authRouter.post("/login")
def login(loginDetails: UserInLogin, session: Session = Depends(get_db)):
    try: 
        return UserService(session=session).login(login_details=loginDetails)
    except Exception as error:
        print(error)
        raise error

@authRouter.post("/signup") 
def signUp(signupDetails: UserInCreate, session: Session = Depends(get_db)):
    try:
        return UserService(session=session).signup(user_details=signupDetails)
    except Exception as error:
        print(error)
        raise error
   