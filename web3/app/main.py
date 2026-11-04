from fastapi import FastAPI, Query, Form
from typing import Annotated
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hand", response_class=HTMLResponse)
async def hand_auth(login: Annotated[str, Query()], password: Annotated[str, Query()]):
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head><meta charset="UTF-8"><title>Авторизация пройдена</title></head>
    <body>
        <h3>Данные авторизации</h3>
        <p><b>Логин:</b> {login}</p>
        <p><b>Пароль:</b> {password}</p>
        <a href="http://localhost:8081/authorization.html">Назад</a>
    </body>
    </html>
    """

class Authorization (BaseModel):
    login: str
    password: str
    model_config = {"extra": "forbid"}

@app.post("/auth", response_class=HTMLResponse)
async def authoriz(auth: Annotated[Authorization, Form()]):
    return f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head><meta charset="UTF-8"><title>Авторизация пройдена</title></head>
        <body>
            <h3>Данные авторизации</h3>
            <p><b>Логин:</b> {auth.login}</p>
            <p><b>Пароль:</b> {auth.password}</p>
            <a href="http://localhost:8081/1_form.html">Назад</a>
        </body>
        </html>
        """

@app.post("/auth-json")
async def auth_json(auth: Authorization) -> Authorization:
    return auth