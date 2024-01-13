from flask import Flask
from .controllers.auth import auth
from .controllers.ocr import ocr
from waitress import serve
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth, url_prefix="/api/v1/auth")
    app.register_blueprint(ocr, url_prefix="/api/v1")
    return app


app = create_app()

app.config["JWT_SECRET"] = os.getenv("JWT_SECRET")


def server():
    if os.getenv("APP_ENV") == "dev":
        app.run(debug=True, port=os.getenv("PORT"), host="0.0.0.0")
    elif os.getenv("APP_ENV") == "prod":
        serve(app, port=os.getenv("PORT"), host="0.0.0.0")
