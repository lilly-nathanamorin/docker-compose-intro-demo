FROM python:3.8.3-slim-buster

RUN apt-get update && apt-get install -y \
  libpq-dev \
  build-essential
RUN mkdir /code
#COPY demo /code/demo
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
WORKDIR /code
CMD ["python", "manage.py", "runserver", "0.0.0.0:8888"]
