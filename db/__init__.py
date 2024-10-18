from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип бд(sqlite, postgres)
SQLALCHEMY_DATABASE_URI = "sqlite:///quiz.db"

# Создаем движок
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Создаем сессию что юы хранить данные
SessionLocal = sessionmaker(bind=engine)

# Создаем полноценную базу
Base = declarative_base()


# Создаем функцию для подключения к бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
