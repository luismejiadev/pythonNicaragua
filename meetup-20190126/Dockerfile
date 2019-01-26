FROM python:3

ENV SRC=python_ni_app
ENV PROJ=/var/www/python_ni_app

COPY $SRC $PROJ

WORKDIR $PROJ

RUN pip install -r requirements.txt