from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_main_page():
    return "Главная страница"


@app.get("/user/admin")
async def get_page_admin():
    return "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def get_user_id(user_id: int):
    return f"Вы вошли как пользователь {user_id}"


@app.get('/user/{first_name}/{last_name}')
async def get_info_about_user(first_name: str, last_name: str, age: int = 100) :
    return f"Информация о пользователе :Имя:{first_name} {last_name}, Возраст:{age}"
