# Задача "Имитация работы с БД":
# Создайте новое приложение FastAPI и сделайте CRUD запросы.
# Создайте словарь users = {'1': 'Имя: Example, возраст: 18'}
# Реализуйте 4 CRUD запроса:
# get запрос по маршруту '/users', который возвращает словарь users.
# post запрос по маршруту '/user/{username}/{age}', который добавляет в словарь по максимальному
# по значению ключом значение строки "Имя: {username}, возраст: {age}". И возвращает строку
# "User <user_id> is registered".
# put запрос по маршруту '/user/{user_id}/{username}/{age}', который обновляет значение из словаря
# users под ключом user_id на строку "Имя: {username}, возраст: {age}". И возвращает строку
# "The user <user_id> is registered"
# delete запрос по маршруту '/user/{user_id}', который удаляет из словаря users по ключу user_id пару.

from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5,
                                                    max_length=30,
                                                    description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description="Enter age",
                                               example="24")]) -> str:
    current_id = str(int(max(users, key=int)) + 1)
    users[current_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {current_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=0,
                                                   le=1000000,
                                                   description="Enter user_id",
                                                   example="24")],
                      username: Annotated[str, Path(min_length=5,
                                                    max_length=30,
                                                    description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description="Enter age",
                                               example="24")]) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=0,
                                                   le=1000000,
                                                   description="Enter user_id",
                                                   example="24")]) -> str:
    users.pop(str(user_id))
    return f"The user {user_id} has been deleted"
