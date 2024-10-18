from sqlalchemy import (Column, Integer, String, DateTime,
                        Boolean, BigInteger, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime


# Cоздаем модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(55), nullable=False)
    phone_number = Column(String, nullable=False)
    level = Column(String, default="Select your level")
    reg_date = Column(DateTime, default=datetime.now())


# Cоздадим модель Question
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, autoincrement=True, primary_key=True)
    main_question = Column(String, nullable=False)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(String, nullable=False)
    timer = Column(DateTime)


# Создадим модель UserAnswer
class UserAnswer(Base):
    __tablename__ = "useranswers"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_answer = Column(String)
    timer = Column(DateTime, default=datetime.now())
    correctness = Column(Boolean, default=False)
    level = Column(String)
    user_fk = relationship(User, lazy="subquery")
    question_fk = relationship(Question, lazy="subquery")


# Cоздадим модель Result
class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    correct_answers = Column(Integer, default=0)
    level = Column(String)

    user_fk = relationship(User, lazy="subquery")