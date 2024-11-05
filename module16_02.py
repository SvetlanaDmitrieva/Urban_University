from typing import Annotated

from attr.validators import min_len
from fastapi import FastAPI, Path
from starlette.responses import PlainTextResponse

app = FastAPI()


@app.get("/user/admin")
async def get_page_admin():
    return "Вы вошли как администратор"


@app.get("/user/{username}/{age}")
async def get_info_about_user(username: Annotated[str, Path(min_length=5,
                                                            max_length=20,
                                                            description="Enter username",
                                                            example="UrbanUser")],
                              age: Annotated[int, Path(ge=18,
                                                       le=120,
                                                       description="Enter age",
                                                       example="24")]):
    return f"Информация о пользователе :Имя:{username} , Возраст:{age}"


@app.get('/user/{user_id}')
async def get_user_id(user_id=Annotated[int, Path(ge=1, le=100,
                                                  description="Enter User ID", example="1")]):
    return f"Вы вошли как пользователь {user_id}"


@app.get("/user/admin")
async def get_page_admin():
    return "Вы вошли как администратор"


@app.get("/")
async def get_main_page():
    return "Главная страница"
