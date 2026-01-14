from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

from app.auth import router
from app.security import SECRET_KEY, ALGORITHM

app = FastAPI()
app.include_router(router, prefix="/authentification")

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(401, "token invalide")

@app.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"user": user}

