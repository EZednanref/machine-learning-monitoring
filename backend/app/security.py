from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "151515"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10
# TODO: add the hashing inside the functions
pwd_context = None  # No longer used

def hash_password(password: str) -> str:
    return password

def verify_password(password: str, hashed: str) -> bool:
    return password == hashed

# Token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

