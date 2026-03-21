from nicegui import app, ui
from Layout import *

@ui.page('/profile')
def Profile():
    maindesign("Profile", 125)
    ui.image('Designs/Banniere_Noire.jpg').style('transform: translate(-5%, -25%); top : 50% ; left : 0%').classes('h-100 w-screen')
    ui.image('Designs/Profil_icon.png').style('transform: translate(-50%, -100%); top : 100% ; left : 10%').classes('h-64 w-64')
    ui.label("@pseudo").style('position: absolute; top: 330px; left: 320px').classes('font-bold text-4xl')
    with ui.card().style('position: absolute; top: 400px; left: 300px').classes(' h-60 w-110').style('background-color: #d293d2; border-radius: 10px; box-shadow: 0px 0px 10px #8030c0'):
        ui.label(f'Biographie...')
    ui.button("Modifier Le Profil", on_click=lambda: ui.navigate.to('/paramètres')).style('position: absolute; transform: translate(-50%, -50%); top: 320px; left: 85%; width: 20%; height: 10%; border-radius: 40px')
    ui.separator().style('position: absolute; top: 660px; left: 300px; width: 60%; height: 0.4%')
    
ui.run()