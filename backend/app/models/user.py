from app.db.postgresql.base_class import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
