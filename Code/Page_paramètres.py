from nicegui import app, ui
from Layout import *
import Layout
import Friend_Circle_Main as fcm
from Database import *

@ui.page('/parametres')
def parametres():
    maindesign("Paramètres", 125)

    user_id = app.storage.user['user_id']  # ← plus de USER_ID fixe
    config = load_config()
    
    user = config[user_id]
    ui.label('PARAMÈTRES').classes('text-3xl font-bold')

    name = ui.input('Pseudo', value=user['username'])
    password = ui.input('Mot de passe', value=user['password'], password=True, password_toggle_button=True)
    bio = ui.textarea('Bio', value=user['bio'])

    def save():
        user_id = app.storage.user['user_id']  # ← récupère l'id de la session
        config[user_id]['username'] = name.value
        config[user_id]['password'] = password.value
        config[user_id]['bio'] = bio.value

        save_config(config)
        ui.notify('Sauvegardé !')
    
    ui.button('Sauvegarder', on_click=save)
    ui.button('Retour', on_click=lambda: ui.navigate.to('/profile'))
    switch()
    ui.button('Se déconnecter', on_click=lambda: ui.navigate.to('/logout')).style('color: red')
    
def changer_theme(e): # C'est ici qu'on insère les thèmes qu'on veut
    global theme_sombre
    Layout.theme_sombre = e.value
    if e.value == "Violet":
        Layout.fond = bgrose
        Layout.fondsecondaire = rosemoyen
        Layout.couleurcontour = violetfoncé
        Layout.couleurbouton = violet
        Layout.couleurcalendrier = rosemoyen
        Layout.couleurlogo = rose
        Layout.couleurcontourlogo = violet
        Layout.couleurtexte1 = noir
        Layout.couleurtexte2 = blanc
    elif e.value == "Radioactif":
        Layout.fond = bgvertsombre
        Layout.fondsecondaire = vertclair
        Layout.couleurcontour = vertfoncé
        Layout.couleurbouton = vert
        Layout.couleurcalendrier = vert
        Layout.couleurlogo = vertclair
        Layout.couleurcontourlogo = vert
        Layout.couleurtexte1 = blanc
        Layout.couleurtexte2 = noir
    elif e.value == "Cerisier":
        Layout.fond = bgblanc2
        Layout.fondsecondaire = rosetrèsclair
        Layout.couleurcontour = beigeclair
        Layout.couleurbouton = rose2
        Layout.couleurlogo = rosetrèsclair
        Layout.couleurcontourlogo = rose2
        Layout.couleurcalendrier = beigeclair
        Layout.couleurtexte1 = noir
        Layout.couleurtexte2 = noir

    ui.navigate.reload() # Raffraichi la page

def switch(): # La fonction qui permet au bouton de fonctionner
    ui.select(
        options=['Radioactif', 'Violet', 'Cerisier'],
        value=Layout.theme_sombre,  
        on_change=changer_theme
    ).style(f'background-color: {Layout.couleurbouton}; border-radius: 10px').classes('px-2').props('push')