FROM python:3-alpine

ADD requirements.txt /
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps
COPY templates /templates
ADD server.py /
EXPOSE 5000
CMD gunicorn -w 2 -b 0.0.0.0:5000 --timeout 500 server:app