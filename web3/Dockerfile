FROM nginx:latest as stat
COPY ./static /usr/share/nginx/html
EXPOSE 80

FROM python:3.12-alpine as app
WORKDIR /fastapi
COPY ./requirements.txt /fastapi/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt
COPY ./app /fastapi/app

EXPOSE 8082
CMD ["fastapi", "run", "app/main.py", "--port", "8082"]





