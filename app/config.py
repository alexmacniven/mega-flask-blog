import os


class Config(object):
    # Used for cryptography, and WTF will use it to protect us
    # pesky CSRF attacks.
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
