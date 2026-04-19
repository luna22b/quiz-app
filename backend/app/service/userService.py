from app.db.repository.userRepo import UserRepo
from app.db.schemas.user import UserOutput, UserInCreate, UserInLogin, UserWithToken
from app.core.security.hashHelper import HashHelper
from app.core.security.authHandler import AuthHandler
from sqlalchemy.orm import Session
from fastapi import HTTPException

class UserService:
    def __init__(self, session: Session):
        self.__userRepo = UserRepo(session = session)
    
    def signup(self, user_details: UserInCreate) -> UserOutput:
        if self.__userRepo.user_exist_by_email(email = user_details.email):
            raise HTTPException(status_code=400, detail="Please login")
        
        hashed_password = HashHelper.get_password_hash(plain_password=user_details.password)
        user_details.password = hashed_password
        return self.__userRepo.create_user(user_data=user_details)
    
    def login(self, login_details: UserInLogin) -> UserWithToken:
        if not self.__userRepo.user_exist_by_email(email = login_details.email):
            raise HTTPException(status_code=400, detail="Please create an account")
        
        user = self.__userRepo.get_user_by_email(email = login_details.email)
        if HashHelper.verify_password(plain_password=login_details.password, hashed_password=user.password):
            token = AuthHandler.sign_jwt(user_id=user.id)
            if token: 
                return UserWithToken(token=token)
            else: 
                raise HTTPException(status_code=500, detail="Unable to process request")
        raise HTTPException(status_code=400, detail="Please check your credentials")    
