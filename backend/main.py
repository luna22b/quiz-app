from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.utils.init_db import create_tables
from fastapi.middleware.cors import CORSMiddleware
from app.routers.auth import authRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialize db at start
    create_tables()
    yield
    
app = FastAPI(lifespan=lifespan)
app.include_router(router=authRouter, tags=["auth"])

origins = [
    "http://localhost:5173", # frontend 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "Running..."}

@app.get("/")
def home():
    return {"message": "API is running"}