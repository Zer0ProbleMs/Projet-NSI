import configparser
import os
from functools import wraps  # ← manquait ça
from nicegui import app, ui  # ← manquait ça aussi

FILE = os.path.join(os.path.dirname(__file__), "users.ini")

def load_config():
    config = configparser.ConfigParser()
    config.read(FILE, encoding="utf-8")
    return config

def save_config(config):
    with open(FILE, "w", encoding="utf-8") as f:
        config.write(f)

def get_all_user_ids():
    config = load_config()
    return [s for s in config.sections() if s.startswith("user_") and s != "user_0"]

def verify_login(username, password):
    """Retourne l'user_id si correct, None sinon."""
    config = load_config()
    for section in config.sections():
        if section.startswith("user_") and section != "user_0":
            if (config[section].get("username") == username and
                    config[section].get("password") == password):
                return section
    return None

def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not app.storage.user.get('user_id'):
            ui.navigate.to('/login')
            return
        return func(*args, **kwargs)
    return wrapper

def get_amis(user_id):
    config = load_config()

    return [
        uid for uid in config.sections()
        if uid.startswith("user_") and uid != user_id
    ]