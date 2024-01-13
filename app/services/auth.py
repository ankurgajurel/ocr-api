from ..database.user import fetch_password_hash

def authenticate_password(username: str, password: str) -> bool:
    password_in_db = fetch_password_hash(username)
    if password_in_db and password == password_in_db:
        return True
    
    return False