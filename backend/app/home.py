from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database import get_db
from app.security import protected
home_router = APIRouter()

@home_router.get("/metriques")
def get_metrics(user=protected):
    db = get_db()
    cur = db.cursor()
    if (cur.execute("SELECT role FROM users where username=%s", (user.username,)) != "admin"):
        print(f"Accès refusé: utilisateur {user.username} non administrateur.")
        raise HTTPException(status_code=403, detail="Accès refusé : manque des droits administrateur")
    else:
        # TODO: implement metrics retrieval from local user pc
        # show_metrics()
        print("AFFICHAGE DES MÉTRIQUES")
