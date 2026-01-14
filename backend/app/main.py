from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from jose.exceptions import ExpiredSignatureError, JWTError

from app.auth import router
from app.security import SECRET_KEY, ALGORITHM
from fastapi import Request
app = FastAPI()
app.include_router(router, prefix="/authentification")

security = HTTPBearer()

def get_current_user(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="non authentifié")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="token expiré")
    except JWTError:
        raise HTTPException(status_code=401, detail="token invalide")

@app.get("/protected")
def protected(user=Depends(get_current_user)):
    return {"user": user}

