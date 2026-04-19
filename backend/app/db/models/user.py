from app.core.database import Base
from sqlalchemy import Column, Integer, String

class User(Base): 
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(70), unique=True, nullable=False)
    password = Column(String(250), nullable=False)