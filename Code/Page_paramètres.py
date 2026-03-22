from nicegui import app, ui
from Layout import *
import Layout

@ui.page('/paramètres')
def paramètres():
    maindesign("Paramètres", 125, Layout.bgact, Layout.c1act, Layout.c2act, Layout.t1act)

    modification()
    switch()
    
def modification():
    ui.label("> Modifier le profil").style(f'{police3}').classes('font-extrabold text-6xl')
    ui.input('pseudo', validation=lambda value: 'Too short' if len(value) < 5 else None)
    ui.input(label='Mot De Passe', placeholder='mot de passe',
        validation={'Input too long': lambda value: len(value) < 20})
    result = ui.label()

def changer_theme(e):
    global theme_sombre
    Layout.theme_sombre = e.value
    if e.value:
        Layout.bgact = bgbleumerfoncé
        Layout.c1act = bleufoncé
        Layout.c2act = bleumer
        Layout.t1act = rouge
    else:
        Layout.bgact = bgrose
        Layout.c1act = violet
        Layout.c2act = violetfoncé
        Layout.t1act = rose

    ui.navigate.reload()  # reloads current page

def switch():
    thème = ui.switch(value=Layout.theme_sombre, on_change=changer_theme)

ui.run()