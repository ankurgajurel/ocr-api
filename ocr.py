from PIL import Image
import pytesseract
import numpy as np

filename = 'sample.png'
img2 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img2)
print(text)