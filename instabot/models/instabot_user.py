from peewee import CharField, IntegerField

from .base import BaseModel


class InstabotUser(BaseModel):
    """
    Instabot user is used for authentication and using Instabot
    """
    user_id = IntegerField(unique=True)
    username = CharField(unique=True)
    password = CharField()
