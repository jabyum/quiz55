from fastapi import APIRouter
from db.userservice import *
user_router = APIRouter(prefix="/user",
                        tags=["Пользовательская часть"])
# регистрация юзера
@user_router.post("/register")
async def register_user(username: str, phone_number: str,
                        level: str = "easy"):
    result = add_user_db(username=username, phone_number=phone_number,
                level=level)
    if result:
        return {"status": 1, "message": "вы удачно зарегистрировались"}
    return {"status": 0, "message": "ошибка регистрации"}

# получение всех пользователей
@user_router.get("/get-users")
async def get_users():
    all_users = get_all_users_db()
    if all_users:
        return {"status": 1, "message": all_users}
    return {"status": 0, "message": "юзеры не найдены"}
