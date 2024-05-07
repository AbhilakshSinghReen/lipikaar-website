FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . /app

CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "ocr_app.wsgi:application"]
