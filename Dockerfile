FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY req.txt /usr/src/app
RUN pip install -r req.txt

COPY . .