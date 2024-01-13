from flask_sqlalchemy import SQLAlchemy
from ..server import app
import os

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()