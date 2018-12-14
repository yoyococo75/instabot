from .base import BaseModel
from peewee import IntegerField, CharField


class User(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField(unique=True)
    password = CharField()
