FROM python:3.6

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt


