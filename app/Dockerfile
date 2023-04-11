FROM python:3-alpine

RUN apk update

WORKDIR /usr/src/app

COPY requirements.txt ./

# Insired by: https://github.com/blurrcat/alpine-python-psycopg2/blob/master/Dockerfile
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY . .

ADD https://raw.githubusercontent.com/eficode/wait-for/master/wait-for .

RUN chmod +x ./wait-for

CMD [ "python", "./app.py" ]
