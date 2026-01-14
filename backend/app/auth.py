from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.security import verify_password, create_access_token, hash_password
from app.database import get_db, delete_user

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/inscription")
def register(user: UserCreate):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "SELECT id FROM users WHERE username=%s",
        (user.username,)
    )
    if cur.fetchone():
        raise HTTPException(status_code=400, detail="Utilisateur déjà existant")

    hashed_password = hash_password(user.password)

    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (user.username, hashed_password)
    )
    db.commit()

    return {"message": "utilisateur créé"}


@router.post("/connexion")
def login(user: UserLogin):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "SELECT password, role FROM users WHERE username=%s",
        (user.username,)
    )
    row = cur.fetchone()

    if not row or not verify_password(user.password, row[0]):
        raise HTTPException(status_code=401, detail="mauvaises infos de connexion")

    token = create_access_token({"sub": user.username,"role": row[1]})

    return {"access_token": token}


@router.post("/suppression")
def suppr(user: UserLogin):
    db = get_db()
    rs = delete_user(user.username, db)    
    if not rs:
        return {"message": "erreur lors de la suppression de l'utilisateur"}
    return {"message": "utilisateur supprimé"}
    
