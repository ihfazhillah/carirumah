FROM python:3.6

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
COPY requirements-dev.txt /app/requirements-dev.txt
WORKDIR /app

RUN pip install -r requirements-dev.txt


