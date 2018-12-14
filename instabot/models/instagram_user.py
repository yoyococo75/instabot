from peewee import BooleanField, CharField, ForeignKeyField, IntegerField

from .base import BaseModel
from .instabot_user import InstabotUser


class InstagramUser(BaseModel):
    """
    Instagram user is used for caching and for reduce requests to Instagram
    """

    instabot_user = ForeignKeyField(InstabotUser, backref="instagram_user", null=True)
    user_id = IntegerField(unique=True)
    username = CharField(unique=True)
    is_private = BooleanField()
    is_business = BooleanField()
    is_verified = BooleanField()
    media_count = IntegerField()
    follower_count = IntegerField()
    following_count = IntegerField()
