from flask import Blueprint, request
from app.middlewares.auth import token_required
from ..services.ocr import process_image

ocr = Blueprint("ocr", __name__)

@ocr.route("/ocr", methods=["POST"])
@token_required
def ocr_api():
    if "file" not in request.files:
        return "Attach a file in request body"
    file = request.files["file"]
    try:
        text = process_image(file.stream)
        return {
            "message": {
                "ocrText": text,
            }
        }
    except Exception as e:
        return {"message": "Error: " + str(e)}