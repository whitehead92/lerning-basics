FROM python:3.12-alpine

WORKDIR /site

COPY server.py .
COPY ./html /site

EXPOSE 8080

CMD ["python", "-u", "server.py"]