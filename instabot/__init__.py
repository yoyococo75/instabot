from .api import API
from .bot import Bot
from .utils import db, utils

assert all((API, Bot, db, utils))  # silence pyflakes
