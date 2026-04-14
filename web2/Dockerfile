FROM python:3.12-alpine

WORKDIR /site

COPY server.py .
COPY ./html /site

EXPOSE 8000

CMD ["python", "-u", "server.py"]