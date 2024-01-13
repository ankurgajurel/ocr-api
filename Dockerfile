FROM --platform=linux/amd64 python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev 
COPY . .
CMD ["python", "main.py"]