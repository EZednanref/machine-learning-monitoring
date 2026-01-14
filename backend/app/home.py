from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend import app
from main import protected
from fastapi import Response
from main import app

router = APIRouter()

app.include_router(router, prefix="/authentification")

@router.post("/deconnexion") 
def logout(response: Response):
    response.delete_cookie(key="access_token", path="/", samesite="lax")
    return {"message": "déconnecté"}

@router.post("/contacts") 
def send_mail():
    user = protected()
    return {"message": "mail envoyé"}



