from pydantic import EmailStr, BaseModel


class UserInCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOutput(BaseModel): 
    id: int 
    username: str
    email: EmailStr

class UserInUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserInLogin(BaseModel):
    identifier: str
    password: str

class UserWithToken(BaseModel):
    token: str