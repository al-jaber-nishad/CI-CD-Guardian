# pull official base image
FROM python:3.11.4-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*
    
# set work directory
WORKDIR /usr/src/app


RUN 

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Migrate and load seed data
# RUN python3 manage.py makemigrations
# RUN python3 manage.py migrate
# RUN python3 manage.py loaddata seed_data.json

# Expose and run the server
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]