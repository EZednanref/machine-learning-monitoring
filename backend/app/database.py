import psycopg2
import os

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "ml"),
        user=os.getenv("DB_USER", "ml"),
        password=os.getenv("DB_PASSWORD", "ml")
    )

def delete_user(username: str, db):    
    cur = db.cursor()
    cur.execute(
        "SELECT id FROM users WHERE username=%s",
        (username,)
    )
    if cur.fetchone() is None:
        print(f"User {username} does not exist.")
        return False
    cur.execute(
        "DELETE FROM users WHERE username=%s",
        (username,)
    )
    db.commit()
    cur.close()
    db.close()
    print(f"User {username} deleted successfully.")
    return True
