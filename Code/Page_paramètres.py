from nicegui import app, ui
from Layout import *
import Layout
import Friend_Circle_Main as fcm

@ui.page('/paramètres')
def paramètres():
    maindesign("Paramètres", 125)
    modification()
    switch()
    
def modification():
    ui.label("> Modifier le profile").style(f'{police3}; color: {Layout.couleurtexte1}').classes('font-extrabold text-6xl')
    ui.input('Pseudonyme', validation=lambda value: 'Too short' if len(value) < 5 else None).style(f'background-color: {Layout.couleurbouton}; border-radius: 10px').classes('px-5')
    ui.input(label='Mot De Passe', placeholder='mot de passe',
        validation={'Input too long': lambda value: len(value) < 20}).style(f'background-color: {Layout.couleurbouton}; border-radius: 10px').classes('px-5')
    result = ui.label()

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
ui.run()