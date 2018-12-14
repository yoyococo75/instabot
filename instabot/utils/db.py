from peewee import SqliteDatabase
from os.path import expanduser, join
from .utils import mkdir_p


class DatabaseHelper:
    HOME = expanduser("~/.instabot")
    DB_NAME = "database.db"

    @classmethod
    def db_interface(cls):
        db_path = cls.database_path()

        # create folders
        mkdir_p(cls.HOME)
        db = SqliteDatabase(db_path, pragmas={
            "journal_mode": "wal",
            "cache_size": -1024 * 64
        })

        return db

    @classmethod
    def database_path(cls):
        db_path = join(cls.HOME, cls.DB_NAME)

        return db_path
