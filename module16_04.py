# Задача "Модель пользователя":
# Подготовка:
# Используйте CRUD запросы из предыдущей задачи.
# Создайте пустой список users = []
# Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
# id - номер пользователя (int)
# username - имя пользователя (str)
# age - возраст пользователя (int)
#
# Измените и дополните ранее описанные 4 CRUD запроса:
# get запрос по маршруту '/users' теперь возвращает список users.
# post запрос по маршруту '/user/{username}/{age}', теперь:
# Добавляет в список users объект User.
# id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
# Все остальные параметры объекта User - переданные в функцию username и age соответственно.
# В конце возвращает созданного пользователя.
# put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
# Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.
# delete запрос по маршруту '/user/{user_id}', теперь:
# Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
# В случае отсутствия пользователя выбрасывается исключение HTTPException с описанием "User was not found" и кодом 404.


from typing import Annotated, List
from fastapi import FastAPI, Path,  HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5,
                                                    max_length=30,
                                                    description="Enter username",
                                                    example="UrbanUser")],
                      age: Annotated[int, Path(ge=18,
                                               le=120,
                                               description="Enter age",
                                               example="24")]) -> User:
    current_id = 1 if not users else users[-1].id + 1
    current_user = User(id=current_id, username=username, age=age)
    users.append(current_user)
    return current_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(ge=1,
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
                                               example="24")]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="The User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(ge=1,
                                                   le=1000000,
                                                   description="Enter user_id",
                                                   example="24")]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="The User was not found")
