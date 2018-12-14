from datetime import datetime

from peewee import DateTimeField, Model, Proxy

db = Proxy()


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField()

    class Meta:
        database = db
