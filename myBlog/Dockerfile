FROM python:3.8

ENV PYTHONBUFFERED=1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /code/

EXPOSE 8000




