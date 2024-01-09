FROM --platform=linux/amd64 python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "app.py"]