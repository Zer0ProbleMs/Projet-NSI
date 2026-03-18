from nicegui import app, ui
from Layout import *

@ui.page('/profile')
def Profile():
    layout()
    maindesign("Profile", 125)
    ui.image('Designs\Banniere_Noire.jpg').style('transform: translate(-5%, -25%); top : 50% ; left : 0%').classes('h-100 w-screen')
    ui.image('Designs\Profil_icon.png').style('transform: translate(-50%, -100%); top : 100% ; left : 10%').classes('h-64 w-64')
    ui.label('@PseudoStylé').style('position: absolute; top: 340px; left: 300px; font-size: 1.5rem')
    with ui.card().style('position: absolute; top: 400px; left: 300px').classes(' h-40 w-110').style('background-color: #d293d2; border-radius: 10px; box-shadow: 0px 0px 10px #8030c0'):
        ui.label(f'BIOGRAPHIE')
    ui.button("Modifier Le Profil", on_click=lambda: ui.navigate.to('/modification')).style('position: absolute; transform: translate(-50%, -50%); top: 400px; left: 70%; width: 20%; height: 10%; border-radius: 50px')
    ui.separator().style('position: absolute; top: 660px; left: 300px; width: 60%; height: 0.4%')
    
ui.run()