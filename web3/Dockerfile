FROM nginx:latest as stat
COPY ./static /usr/share/nginx/html
EXPOSE 80

FROM python:3.12-alpine as app
WORKDIR /fastapi
<<<<<<< HEAD
COPY ./requirements.txt /fastapi/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt
COPY ./app /fastapi/app
=======
COPY ./app /fastapi

RUN pip install uv
RUN uv sync --frozen --no-dev
>>>>>>> aefd26e1b2efeb21da50a9e5a64218d76025b1aa
EXPOSE 8082
CMD ["fastapi", "run", "app/main.py", "--port", "8082"]





