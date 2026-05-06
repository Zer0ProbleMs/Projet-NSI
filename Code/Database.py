import configparser
import os

FILE = os.path.join(os.path.dirname(__file__), "users.ini")
USER_ID = "user_0"


def load_config():
    config = configparser.ConfigParser()
    config.read(FILE, encoding="utf-8")
    return config


def save_config(config):
    with open(FILE, "w", encoding="utf-8") as f:
        config.write(f)