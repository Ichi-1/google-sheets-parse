FROM python:3.10.6-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /django_proj

WORKDIR /django_proj

COPY ./backend /django_proj
COPY ./backend/req.txt /django_proj

RUN pip3 install wheel 
RUN pip3 install -r req.txt


