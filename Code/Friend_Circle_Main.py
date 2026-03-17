from nicegui import app, ui
from Layout import *
import uuid 
"""  
Commande que je préfèrerais ne pas oublier:
- .style('border-radius: value;')
- ui.sub.pages({'/': page_function, '/page1': page1_function}) et @ui.page('/')
- La commande "with" qui permet d'ajouter une réponse ou une fonction suivante, comme "with ui.link("lien"):" suivi de "ui.image("image")" qui fait que l'image renvoie à un lien
- .style('box-shadow: value;') qui permet d'enlever les ombres autour d'un objet et .style('background-color: hex color') qui change le fond d'un objet
- ui.row() qui est utilisé pour faire une rangée d'items, souvent associé avec ui.menu()
- Je pense qu'il est possible de créer une fonction pour le signe PLUS qui créera un nouveau ui.card pour chaque calendrier créé par l'utilisateur
-

Ce que je veux pouvoir faire:
- Changer de police de caractère | FAIT
- Arrondir les bordure (tout en gardant le fond transparent) | FAIT
- Déplacer les textes des menu_item vers la gauche
- Avancer sur les paramètres
- Réussir à agrandir les bords de façon animé au clic d'une flèche => bouton. 
- Une flèche qui étant le bord gauche, mais aussi que les différentes flèches sur ce même bords, si le bord n'est pas étendu, alors ces flèches l'étendrons.
- Créer les premier boutons principaux qui mèneront au calendrier choisis
- Un bouton notification et message avec chacun d'entre eux n'ouvrant pas une page mais une simple boîte avec preview et donne l'option d'ouvrir dans une nouvelle page
"""

@ui.page('/')
def main_page():

    if 'calendriers' not in app.storage.general:
        app.storage.general['calendriers'] = []

    @ui.refreshable
    def liste_calendriers():
        with ui.scroll_area().classes('w-full h-195'):
            with ui.grid().classes('grid-flow-col auto-cols-fr gap-4 w-max p-4'):
                for cal in app.storage.general['calendriers']:
                    cal_id = cal['id']
                    with ui.card().classes('w-100 h-176').style('background-color: #d293d2; border-radius: 10px; box-shadow: 0px 0px 10px #8030c0'):
                        ui.label(cal['name']).classes('font-bold text-2xl')
                        with ui.image('Designs/Triple_points.png').classes('w-12 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 85%; top: 5%'):
                            with ui.menu():
                                ui.menu_item("Paramètrage",on_click=lambda cid=cal_id: boite_renommer(cid)).style('background-color: #8030c0; color: #ffffff').classes('py-2 px-25 text-center font-light')
                                ui.menu_item("Supprimer",on_click=lambda cid=cal_id: supprimer_calendrier(cid)).style('background-color: #8030c0; color: #ffffff').classes('py-2 px-25 text-center font-light')
                        ui.button("Ouvrir", on_click=lambda cid=cal_id: ui.navigate.to(f'/calendrier/{cid}')).style('position: absolute; transform: translate(-50%, -50%); top: 90%; left: 50%; width: 75%; height: 15%; border-radius: 50px')

    def ajouter_calendrier():
        new_cal = {'id': str(uuid.uuid4()), 'name': f'Calendrier {len(app.storage.general["calendriers"]) + 1}'}
        app.storage.general['calendriers'].append(new_cal)
        liste_calendriers.refresh()

    def boite_renommer(cal_id):
        cal = next(c for c in app.storage.general['calendriers'] if c['id'] == cal_id)
        with ui.dialog() as dialog, ui.card():
            ui.label('Renommer le calendrier').classes('font-bold text-xl')
            nom_entrée = ui.input('Nouveau nom', value=cal['name'])
            with ui.row():
                ui.button('Annuler', on_click=dialog.close)
                def save_name():
                    cal['name'] = nom_entrée.value
                    app.storage.general['calendriers'] = app.storage.general['calendriers']
                    dialog.close()
                    liste_calendriers.refresh()
                ui.button('Sauvegarder', on_click=save_name).style('background-color: #8030c0; color: white')
        dialog.open()

    def supprimer_calendrier(cal_id):
        app.storage.general['calendriers'] = [c for c in app.storage.general['calendriers'] if c['id'] != cal_id]
        liste_calendriers.refresh()

    accueildesign("Page d'accueil", 125, len(app.storage.general['calendriers']), on_add=ajouter_calendrier)
    liste_calendriers()

ui.run(storage_secret='clé-secrete')