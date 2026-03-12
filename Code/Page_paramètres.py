from nicegui import app, ui
from Layout import *

@ui.page('/paramètres')
def paramètres():
    layout()
    maindesign("Paramètres", 125)
    ui.label("Cette page vous permettra d'acceder à vos différents paramètres")

ui.run()