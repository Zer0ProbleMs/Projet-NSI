from nicegui import ui
from Layout import *
import Layout

@ui.page('/calendrier/{cal_id}')
def Page_Calendrier(cal_id: str):
    calendriers = app.storage.general.get('calendriers', [])
    cal = next((c for c in calendriers if c['id'] == cal_id), None)

    if cal is None:
        ui.label('Calendrier introuvable').classes('text-red-500 text-2xl')
        ui.button('Retour', on_click=lambda: ui.navigate.to('/')).style('background-color: #8030c0; color: white')
        return
    
    maindesign(cal['name'], 125)

ui.run(storage_secret='clé-secrete')