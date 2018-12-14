from datetime import datetime

from peewee import DateTimeField, Model, Proxy

db = Proxy()


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()

        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db
