from nicegui import app, ui
from Layout import *

@ui.page('/modification')
def modification():
    maindesign("Modification", 125)
    ui.label("> Modifier le profil").style('').classes('font-extrabold text-6xl')
    ui.input('pseudo', validation=lambda value: 'Too short' if len(value) < 5 else None)
    ui.input(label='Mot De Passe', placeholder='mot de passe',
        validation={'Input too long': lambda value: len(value) < 20})
    result = ui.label()

ui.run()