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

2. Run the app

```sh
python3 app.py
```

### Docker 

```sh
docker build -t ocr-api .
docker run -p 8000:8000 ocr-api
```

The application should now be running at `http://localhost:8000`.

## Usage

Provide usage instructions here.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details