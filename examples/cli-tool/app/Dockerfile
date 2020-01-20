FROM python:3.8.1-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY micro-curl.py micro-curl.py

ENTRYPOINT ["python3", "micro-curl.py"]
