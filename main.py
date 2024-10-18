from fastapi import FastAPI
from api.user_api.user import user_router
app = FastAPI(docs_url="/")
from db import Base, engine
# создаем бд и делаем все миграции
Base.metadata.create_all(bind=engine)
# регистрация компонентов проекта(роутеров)
app.include_router(user_router)





