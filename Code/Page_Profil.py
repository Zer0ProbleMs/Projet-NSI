from nicegui import ui
from Layout import *
from Database import *
import Layout


@ui.page('/profile')
@require_login
def Profile():
    maindesign("Profile", 125)
    
    user_id = app.storage.user['user_id']  # ← récupère l'id de la session
    config = load_config()

    if user_id not in config:
        ui.label("Utilisateur introuvable")
        return

    user = config[user_id]  # ← manquait cette ligne !

    banner = user.get('banner', 'Designs/Banniere_Noire.jpg')
    profile_pic = user.get('profile_pic', 'Designs/Profil_icon.png')

    ui.image(banner).style(
        'transform: translate(-5%, -25%); top: 50%; left: 0%'
    ).classes('h-100 w-screen')

    ui.image(profile_pic).style(
        'transform: translate(-50%, -100%); top: 100%; left: 10%'
    ).classes('h-64 w-64')

    ui.label(user.get("username", "Pseudo")).style(
        f'position: absolute; top: 330px; left: 320px; color: {Layout.couleurtexte1}'
    ).classes('font-bold text-4xl')

    with ui.card().style(
        f'position: absolute; top: 400px; left: 300px; '
        f'background-color: {Layout.fondsecondaire}; border-radius: 10px; '
        f'box-shadow: 0px 0px 10px {Layout.couleurcontour}'
    ).classes('h-60 w-110'):
        ui.label(user.get("bio", "Pas de bio"))

    ui.button(
        "Modifier Le Profil",
        on_click=lambda: ui.navigate.to('/parametres')
    ).style(
        'position: absolute; transform: translate(-50%, -50%); '
        'top: 320px; left: 85%; width: 20%; height: 10%; border-radius: 40px'
    )

    ui.separator().style(
        'position: absolute; top: 660px; left: 300px; width: 60%; height: 0.4%'
    )

@ui.page('/profil/{user_id}')
def profil_public(user_id: str):
    maindesign("Profile", 125)
    config = load_config()
    
    if user_id not in config:
        ui.label('Utilisateur introuvable')
        return
    
    user = config[user_id]

    banner = user.get('banner', 'Designs/Banniere_Noire.jpg')
    profile_pic = user.get('profile_pic', 'Designs/Profil_icon.png')

    ui.image(banner).style(
        'transform: translate(-5%, -25%); top: 50%; left: 0%'
    ).classes('h-100 w-screen')

    ui.image(profile_pic).style(
        'transform: translate(-50%, -100%); top: 100%; left: 10%'
    ).classes('h-64 w-64')

    ui.label(user.get("username", "Pseudo")).style(
        f'position: absolute; top: 330px; left: 320px; color: {Layout.couleurtexte1}'
    ).classes('font-bold text-4xl')

    with ui.card().style(
        f'position: absolute; top: 400px; left: 300px; '
        f'background-color: {Layout.fondsecondaire}; border-radius: 10px; '
        f'box-shadow: 0px 0px 10px {Layout.couleurcontour}'
    ).classes('h-60 w-110'):
        ui.label(user.get("bio", "Pas de bio"))

    ui.separator().style(
        'position: absolute; top: 660px; left: 300px; width: 60%; height: 0.4%'
    )