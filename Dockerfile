FROM python:3.8
WORKDIR /app

ADD Pipfile /app/Pipfile
ADD Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8001

COPY ./ /app
