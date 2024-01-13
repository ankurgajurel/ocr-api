from .models.user import User

def fetch_password_hash(username: str, password: str) -> str:
    password_hash = User.query.filter_by(username=username).first()
    if password_hash == password:
        return True
    
    return False