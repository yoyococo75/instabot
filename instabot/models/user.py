from peewee import CharField, IntegerField

from .base import BaseModel


class User(BaseModel):
    user_id = IntegerField(unique=True)
    username = CharField(unique=True)
    password = CharField()
