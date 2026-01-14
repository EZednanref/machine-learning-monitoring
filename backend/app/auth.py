from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.security import verify_password, create_access_token, hash_password
from app.database import get_db, delete_user
from fastapi import Response

router = APIRouter()

class UserCreate(BaseModel):
    nom: str
    prenom: str
    username: str
    password: str
    

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/inscription")
def register(user: UserCreate):
    db = get_db()
    cur = db.cursor()
    
    cur.execute("SELECT id FROM users WHERE nom=%s", (user.nom,))
    if cur.fetchone():
        cur.execute("SELECT id FROM users WHERE prenom=%s", (user.prenom,))
        if cur.fetchone():
            raise HTTPException(400, "Vous êtes déjà inscrit")

    cur.execute("SELECT id FROM users WHERE username=%s", (user.username,))
    if cur.fetchone():
        raise HTTPException(400, "Nom d'utilisateur déjà pris")

    hashed_password = hash_password(user.password)

    cur.execute(
        "INSERT INTO users (nom, prenom, username, password) VALUES (%s, %s, %s, %s)",
        (user.nom, user.prenom, user.username, hashed_password)
    )
    db.commit()
    return {"message": "utilisateur créé"}

@router.post("/connexion")
def login(user: UserLogin, response: Response):
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

    response.set_cookie(key="access_token", value=token, httponly=True, secure=False, samesite="lax", path="/")

    return {"message": "Connecté"}


@router.post("/suppression")
def suppr(user: UserLogin):
    db = get_db()
    rs = delete_user(user.username, db)    
    if not rs:
        return {"message": "erreur lors de la suppression de l'utilisateur"}
    return {"message": "utilisateur supprimé"}
    



    