import sqlalchemy

from app.config.db import Base

class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String(64), unique=True)