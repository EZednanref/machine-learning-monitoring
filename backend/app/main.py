from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

from app.auth import auth_router
from app.home import home_router


app = FastAPI()
app.include_router(auth_router, prefix="/authentification")



