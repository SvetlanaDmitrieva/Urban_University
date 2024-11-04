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


@app.get('/user')
async def get_info_about_user(first_name: str = "first_name", age: int = 100) :
    return f"Информация о пользователе :Имя:{first_name} , Возраст:{age}"
