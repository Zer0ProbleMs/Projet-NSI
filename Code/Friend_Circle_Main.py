from nicegui import app, ui
from Layout import *
import Layout
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
- Faire un ui.skeleton pour voir le squelette du site quand il charge (Secondaire)
-	Qd on modifie le pseudo il se modifie sur la base de données et le profil
-	Qd on modifie le mdp ça change sur la base de donnée 
-	Qd on change la photo de profil ça change sur la page profil
-	Qd on change la bannière 
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
                    snapshot = cal.get('snapshot', '')

                    with ui.card().classes('w-100 h-176').style(f'background-color: {Layout.t1act}; border-radius: 10px; box-shadow: 0px 0px 20px {violetfoncé}; overflow:hidden'):
                        ui.label(cal['name']).classes('font-bold text-2xl')

                        # ↓ Snapshot preview iframe
                        ui.html(f'''
                            <div style="position:absolute; top:12%; left:5%; width:90%; height:65%;
                                        border-radius:8px; overflow:hidden; border:2px solid {violetfoncé};
                                        pointer-events:none;">
                                {snapshot}
                            </div>
                        ''', sanitize=False)

                        with ui.image('Designs/Triple_points.png').classes(
                            'w-12 cursor-pointer hover:opacity-80'
                        ).style('position: absolute; transform: translate(-50%, -50%); left: 85%; top: 5%'):
                            with ui.menu().style('transform: translate(-75%, 0%)'):
                                with ui.menu_item("Paramètrage",on_click=lambda cid=cal_id: boite_renommer(cid)).style(f'background-color: {violetfoncé}; color: white').classes('py-2 px-25 text-center font-light text-xl'):
                                    with ui.item_section().props('avatar'):
                                        ui.icon('settings')
                                ui.separator().style(f'background-color: {violet}')
                                with ui.menu_item("Supprimer",on_click=lambda cid=cal_id: supprimer_calendrier(cid)).style(f'background-color: {violetfoncé}; color: white').classes('py-2 px-25 text-center font-light text-xl'):
                                    with ui.item_section().props('avatar'):
                                        ui.icon('delete')
                                ui.separator().style(f'background-color: {violet}')
                                with ui.menu_item('Fermer', ui.menu.close).style(f'background-color: {violetfoncé}; color: white').classes('py-2 px-25 text-center font-light text-xl'):
                                    with ui.item_section().props('avatar'):
                                        ui.icon('close')

                        ui.button("Ouvrir",on_click=lambda cid=cal_id: ui.navigate.to(f'/calendrier/{cid}')).style(f'position: absolute; transform: translate(-50%, -50%); top: 90%; left: 50%; width: 75%; height: 15%; border-radius: 50px; {police1}').classes('text-xl font-bold')

    def generer_snapshot(name: str) -> str:
        jours = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
        
        header = ''.join(
            f'<div style="background: {violetfoncé}; color: white; text-align: center; font-size: 10px; padding: 2px; order-radius: 2px">{j}</div>'
            for j in jours
        )
        days = ''.join(
            f'<div style="background: {rose}; color: white; text-align: center; font-size: 10px; padding: 2px; border-radius: 2px">{i}</div>'
            for i in range(1, 32)
        )
        
        cell = f'background: {violetfoncé}; color: white; text-align: center; font-size: 10px; padding: 2px; border-radius: 2px'
        grid_style = 'display: grid; grid-template-columns: repeat(7,1fr); gap: 2px; margin-bottom: 6px'
        
        return (
            f'<div style="margin: 0; padding: 8px; background: {rosemoyen}; font-family: sans-serif; overflow: hidden; height: 100%">'
            f'<div style="font-weight: bold; font-size: 14px; color: {violettrèsfoncé}; margin-bottom: 6px">Aperçu</div>'
            f'<div style="{grid_style}">{header}{days}</div>'
            f'<div style="color: {violettrèsfoncé}; font-size: 10px; font-style: italic">Aucun évènement</div>'
            f'</div>'
        )
        
    def ajouter_calendrier():
        new_cal = {
            'id': str(uuid.uuid4()),
            'name': f'Calendrier {len(app.storage.general["calendriers"]) + 1}',
            'snapshot': generer_snapshot('placeholder')  # ← simpler call
        }
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
                ui.button('Sauvegarder', on_click=save_name).style(f'background-color: {violetfoncé}; color: white')
        dialog.open()

    def supprimer_calendrier(cal_id):
        app.storage.general['calendriers'] = [c for c in app.storage.general['calendriers'] if c['id'] != cal_id]
        liste_calendriers.refresh()

    if Layout.theme_sombre:
        accueildesign("Page d'accueil", 125, bgbleumerfoncé, bleufoncé, bleumer, rouge, len(app.storage.general['calendriers']), on_add=ajouter_calendrier)
    else:
        accueildesign("Page d'accueil", 125, bgrose, violet, violetfoncé, rose, len(app.storage.general['calendriers']), on_add=ajouter_calendrier)
    
    liste_calendriers()

ui.run(storage_secret='clé-secrete')