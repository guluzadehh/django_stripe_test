FROM python:3.10.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN mkdir /wd
WORKDIR /wd

RUN pip install --upgrade pip

COPY requirements.txt /wd
RUN pip install -r requirements.txt

COPY . /wd

# RUN sh -c "cd app/ && python manage.py makemigrations && python manage.py migrate"

# CMD [ "python", "app/manage.py", "runserver", "0.0.0.0:8000"]
