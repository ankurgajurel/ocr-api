from PIL import Image
import pytesseract
import numpy as np

def process_image(file_stream):
    img = Image.open(file_stream)
    img2 = np.array(img)
    text = pytesseract.image_to_string(img2)
    return text