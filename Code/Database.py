import configparser
import os
from functools import wraps  # ← manquait ça
from nicegui import app, ui  # ← manquait ça aussi
import json
from datetime import datetime

FILE = os.path.join(os.path.dirname(__file__), "users.ini")

def load_config():
    config = configparser.ConfigParser(interpolation=None)
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


def get_user_calendars(user_id):
    config = load_config()

    if user_id not in config:
        return []

    if 'calendars' not in config[user_id]:
        config[user_id]['calendars'] = '[]'
        save_config(config)

    try:
        return json.loads(config[user_id]['calendars'])
    except:
        return []

def save_user_calendars(user_id, calendars):
    config = load_config()

    if user_id not in config:
        return

    config[user_id]['calendars'] = json.dumps(calendars)
    save_config(config)

def ajouter_notification(destinataire_pseudo, de_pseudo, message_texte):
    # Trouve l'ID du destinataire par son pseudo et lui ajoute une notification à la cloche
    config = load_config()
    destinataire_id = None
    
    # Parcourt les utilisateurs pour l'associer au bon ID (par exemple: user_1)
    for section in config.sections():
        if section.startswith("user_") and section != "user_0":
            if config[section].get("username") == destinataire_pseudo:
                destinataire_id = section
                break
                
    if not destinataire_id:
        return # Si l'utilisateur n'est pas trouvé, le programme fait rien
        
    notifs = app.storage.general.get('global_notifications', {})
    if destinataire_id not in notifs:
        notifs[destinataire_id] = []
        
    notifs[destinataire_id].append({
        'from': de_pseudo,
        'text': message_texte
    })
    app.storage.general['global_notifications'] = notifs

def obtenir_notifications(user_id):
    # Récupère la liste des notifications de l'utilisateur qui est connecté
    notifs = app.storage.general.get('global_notifications', {})
    return notifs.get(user_id, [])

def vider_notifications(user_id):
    # Vide la liste des notifications ("marquer comme lu")
    notifs = app.storage.general.get('global_notifications', {})
    if user_id in notifs:
        notifs[user_id] = []
        app.storage.general['global_notifications'] = notifs

def trouver_calendrier_par_id(cal_id):
    # Cherche un calendrier chez tous les utilisateurs.
    import json
    config = load_config()
    for section in config.sections():
        if section.startswith("user_") and section != "user_0":
            try:
                cals = json.loads(config[section].get('calendars', '[]'))
            except:
                cals = []
            for c in cals:
                if c.get('id') == cal_id:
                    return section, c, cals
    return None, None, None

def get_calendriers_partages(user_id):
    # Trouve les calendriers que les autres ont partagés avec moi.
    import json
    config = load_config()
    partages = []
    for section in config.sections():
        if section.startswith("user_") and section != user_id and section != "user_0":
            try:
                cals = json.loads(config[section].get('calendars', '[]'))
            except:
                cals = []
            for c in cals:
                shared_with = c.get('shared_with', {})
                if user_id in shared_with:
                    partages.append({
                        'owner_id': section,
                        'owner_name': config[section].get('username', 'Inconnu'),
                        'cal': c,
                        'permission': shared_with[user_id]
                    })
    return partages