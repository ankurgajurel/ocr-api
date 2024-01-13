from functools import wraps
from flask import request, jsonify
from jwt import decode, exceptions
import os


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not request.authorization:
            return {"success": False, "message": "Token is missing."}, 401
        access_token = str(request.authorization).split(" ")[1]
        try:
            data = decode(access_token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
        except exceptions.InvalidTokenError:
            return jsonify({"message": "Token is invalid!"}), 401
        return f(*args, **kwargs)

    return decorated
