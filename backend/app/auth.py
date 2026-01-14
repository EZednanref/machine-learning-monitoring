from fastapi import APIRouter, HTTPException
from app.security import verify_password, create_access_token
from app.database import get_db

router = APIRouter()

@router.post("/inscription")
def register(username: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute("SELECT id FROM users WHERE username=%s", (username,))
    if cur.fetchone():
        raise HTTPException(400, "Utilisateur déjà existant")

    cur.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (username, password)
    )
    db.commit()
    return {"message": "utilisateur créé"}

@router.post("/connexion")
def login(username: str, password: str):
    db = get_db()
    cur = db.cursor()

    cur.execute(
        "SELECT password, role FROM users WHERE username=%s",
        (username,)
    )
    user = cur.fetchone()
    if not user or not verify_password(password, user[0]):
        raise HTTPException(401, "mauvaises infos de connexion")

    token = create_access_token({"sub": username, "role": user[1]})
    return {"access_token": token}

