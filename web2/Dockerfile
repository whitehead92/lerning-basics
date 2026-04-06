FROM python:3.12-alpine

WORKDIR /site

COPY ./html /site

EXPOSE 8000

CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", "/site"]