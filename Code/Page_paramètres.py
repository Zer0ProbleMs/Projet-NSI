from nicegui import app, ui
from Layout import *
import Layout

@ui.page('/paramètres')
def paramètres():
    maindesign("Paramètres", 125, Layout.bgact, Layout.c1act, Layout.c2act, Layout.t1act)
    modification()
    switch()
    
def modification():
    ui.label("> Modifier le profil").style(f'{police3}, color: {Layout.ctexte}').classes('font-extrabold text-6xl')
    ui.input('pseudo', validation=lambda value: 'Too short' if len(value) < 5 else None).style(f'color: {Layout.ctexte}')
    ui.input(label='Mot De Passe', placeholder='mot de passe',
        validation={'Input too long': lambda value: len(value) < 20}).style(f'color: {Layout.ctexte}')
    result = ui.label()

def changer_theme(e):
    global theme_sombre
    Layout.theme_sombre = e.value
    if e.value == "violet":
        Layout.bgact = bgrose
        Layout.c1act = violet
        Layout.c2act = violetfoncé
        Layout.t1act = rose
        Layout.ctexte = noir
    elif e.value == "radioactif":
        Layout.bgact = bgvertsombre
        Layout.c1act = vertfoncé
        Layout.c2act = vertclair
        Layout.t1act = vert
        Layout.ctexte = blanc
    elif e.value == "océan":
        Layout.bgact = bgbleumerfoncé
        Layout.c1act = bleumer
        Layout.c2act = bleufoncé
        Layout.t1act = bleumerfoncé
        Layout.ctexte = blanc


    ui.navigate.reload()  # reloads current page

def switch():
    ui.select(
        options=['radioactif', 'violet', 'océan'],
        value=Layout.theme_sombre,  # default selected
        on_change=changer_theme
    ).style('background-color: #ffffff')
ui.run()