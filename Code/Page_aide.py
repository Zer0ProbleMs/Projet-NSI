from nicegui import *
from Layout import *

@ui.page('/aide')
def aide():
    designaide("Aide", 300)
    ui.label("Général").classes('text-4xl font-bold')
    ui.separator()
    ui.label("Bienvenue sur notre site web! Si vous vous retrouvez sur cette page, cela veut dire que vous avez besoin d'une aide de tel sorte. Ainsi, voici une général:").classes('text-2xl font-light text-center')
    ui.separator()
    ui.label("> Ici, vous vous trouvez sur notre page aide. Vous l'avez atteinte en appuyant sur le point d'interrogation que vous pouvez voir dans le coin en bas à gauche.").classes('text-2xl font-light')
    ui.label("> Vous pouvez également accéder à d'autre page, par exemple, notre page d'accueil peut-être accédé en appuyant sur notre logo \"Friend Circle + \".").classes('text-2xl font-light')

    
ui.run()