from flask import Flask, request

from PIL import Image
import pytesseract
import numpy as np

app = Flask(__name__)

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
    app.run(debug=True, port=8000, host='0.0.0.0')