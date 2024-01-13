from flask import Blueprint, request
from jwt import encode
import datetime
import os

from werkzeug.security import generate_password_hash

auth = Blueprint("auth", __name__)

creds = {"username": "ankur", "password": "ankur12345"}

@auth.route("/login")
def login():
    auth = request.authorization
    if (
        auth
        and auth.password == creds["password"]
        and auth.username == creds["username"]
        and auth.password == creds["password"]
    ):
        token = encode(
            {
                "user": auth.username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
            },
            os.getenv("JWT_SECRET"),
        )
        return {"success": True, "token": token}, 200
    return (
        {
            "success": False,
            "message": "Incorrect Password or Username. Please try again.",
        },
        401,
        {"WWW-Authenticate": 'Basic realm="Login Required"'},
    )

@auth.route('/register', methods=['POST'])
def register():
    creds = request.get_json()
    username = creds.get('username')
    password = creds.get('password')

    if not username or not password:
        return {"success": False, "message": "Username and password are required"}, 400

    hashed_password = generate_password_hash(password)

    return {"success": True, "message": "User registered successfully"}, 201


@auth.route("/sample")
def sample():
    return {"success": True, "message": "This is a sample route"}
