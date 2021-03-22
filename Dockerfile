FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000