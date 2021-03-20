FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

EXPOSE 8000