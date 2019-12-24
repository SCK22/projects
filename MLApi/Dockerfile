# name of the image
# multi stage build
# FROM ubuntu:16.04
FROM alpine:3.8
FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . /app

WORKDIR /app
# run pip install for installing the requrements
RUN pip3 install -r requirements.txt
RUN python -m spacy download en_core_web_sm
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]
