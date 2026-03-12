from nicegui import app, ui
from Layout import *

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
def Main_page():
    layout()
    ncal = 0
    accueildesign("Page d\'accueil", 125, ncal)
    with ui.scroll_area().classes('w-full h-195'):
        with ui.grid().classes('grid-flow-col auto-cols-fr gap-4 w-max p-4'):
            for i in range(ncal):
                with ui.card().classes('w-100 h-176').style('background-color: #d293d2; border-radius: 10px; box-shadow: 0px 0px 10px #8030c0'):
                    ui.label(f'Calendrier {i+1}').classes('font-bold text-2xl')
                    with ui.row().classes('justify-end items-center gap-2'):
                        with ui.image('Designs\Triple_points.png').classes('w-12 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 85%; top: 5% '):
                            with ui.menu() as menu:
                                ui.menu_item("Hello").style('background-color: #8030c0; color: #ffffff').classes('py-2 px-25 text-center font-light left') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
                    ui.button("Ouvrir", on_click=lambda: ui.navigate.to('/calendrier')).style('position: absolute; transform: translate(-50%, -50%); top: 90%; left: 50%; width: 75%; height: 15%; border-radius: 50px')
                
            
ui.run()