# OCR Application

This is an OCR (Optical Character Recognition) application built with Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Tessaract
- Python
- Docker if you want to run it in a container

### Installation

1. Clone and Navigate to Repo

```sh
git clone https://github.com/ankurgajurel/ocr-api
```

2. Virtual Env and dependencies

```sh
sudo virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy Environment Variables

```sh
cp .env.example .env
```

3. Run the app

```sh
python3 main.py
```

### Docker

```sh
docker build -t ocr-api .
docker run -p 8000:8000 ocr-api
```

The application should now be running at `http://localhost:8000`.

## API Endpoints

### POST /api/ocr

This endpoint allows you to perform OCR on an image.

## Sample Request

#### Python Request

You can use the `requests` library in Python to make a POST request to the API.

```python
import requests

url = "https://ocr-api.ankurgajurel.com.np/ocr"
file_path = "sample.png"

with open(file_path, "rb") as file:
    response = requests.post(url, files={"file": file})

print(response.json())
```

### JavaScript Request

You can use the fetch API in JavaScript to make a POST request to the API.

```javascript
const url = "https://ocr-api.ankurgajurel.com.np/ocr";
const file = document.querySelector('input[type="file"]').files[0];

const formData = new FormData();
formData.append("file", file);

fetch(url, {
  method: "POST",
  body: formData,
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details
