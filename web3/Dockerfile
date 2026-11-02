FROM nginx:latest as stat
COPY ./static /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM python:3.12-alpine as app
WORKDIR /fastapi
COPY ./app /fastapi

RUN pip install --no-cache-dir uv
RUN uv sync --frozen --no-dev
EXPOSE 8082
CMD ["uv", "run", "python", "main.py"]





