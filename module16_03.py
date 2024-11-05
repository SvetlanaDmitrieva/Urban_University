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

from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    current_id = str(int(max(users, key = int)) + 1)
    users[current_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {current_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f"The user {user_id} has been deleted"
