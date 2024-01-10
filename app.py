from flask import Flask, request
from waitress import serve

from PIL import Image
import pytesseract
import numpy as np

import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/')
def index():
    return {'message': 'Hello World'}

@app.route('/ocr', methods=['POST'])
def ocr():
    if('file' not in request.files):
        return 'Attach a file in request body'
    file = request.files['file']
    try:
        img = Image.open(file.stream)
        img2 = np.array(img)
        text = pytesseract.image_to_string(img2)
        return {"message": {
        "ocrText": text,
    }}
    except Exception as e:
        return {"message": "Error: " + str(e)}

if __name__ == '__main__':
    if os.getenv("APP_ENV") == "dev":
        print("Running in Development")
        app.run(debug=True, port=8000, host='0.0.0.0')
    elif os.getenv("APP_ENV") == "prod":
        print("Running in Production")
        serve(app, port=os.getenv("PORT"), host='0.0.0.0')