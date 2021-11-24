FROM python:3.7-alpine 

ENV PYTHONDONTWRITEBYCODE 1 
ENV PYTHONUNBUFFERED 1 

WORKDIR /app

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev zlib-dev
RUN apk add postgresql-dev 

RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY ./entrypoint.sh .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
