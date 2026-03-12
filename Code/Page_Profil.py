from nicegui import app, ui
from Layout import *

@ui.page('/profile')
def Profile():
    layout()
    maindesign("Profile", 125)
    ui.label("Cette page sera construite par Anfel, mais ceci est un placeholder")
    ui.link('>Retourner à la page d\'accueil<', '/')

ui.run()