from Database import get_user_calendars, save_user_calendars
from nicegui import app, ui
from Layout import *
import Layout
import uuid 
"""  
Commande que je préfèrerais ne pas oublier:
- .style('border-radius: value;')
- @ui.page('/')
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
def main_page(): # Fonction de la page principale

    user_id = app.storage.user.get('user_id')

    if not user_id:
        ui.navigate.to('/login')
        return

    def get_calendriers():
        return get_user_calendars(user_id)

    @ui.refreshable
    def liste_calendriers():
        calendriers = get_calendriers()
        with ui.row().classes('w-full gap-6 p-4'): # Légèrement augmenté l'espace entre les cartes (gap-6)
            for cal in calendriers:
                # Chaque carte de calendrier - CHANGEMENT : w-72 h-80 (plus grande) au lieu de w-64 h-64
                with ui.card().classes('w-95.5 h-150 shadow-lg flex flex-col justify-between').style(
                    f'background-color: {Layout.couleurcalendrier}; border-radius: 15px; position: relative;'):
                    
                    # Entête de la carte (Nom + Menu options)
                    with ui.row().classes('w-full justify-between items-center'):
                        ui.label(cal['name']).classes('font-bold text-xl text-white truncate').style('max-width: 180px')
                        
                        # Menu trois points pour renommer/supprimer
                        # AJOUT de .classes('stop-propagation') pour bloquer le clic sur la carte !
                        with ui.button(icon='more_vert').props('flat round dense').classes('stop-propagation').style('color: white'):
                            with ui.menu():
                                ui.menu_item('Renommer', on_click=lambda c=cal['id']: boite_renommer(c))
                                ui.menu_item('Supprimer', on_click=lambda c=cal['id']: supprimer_calendrier(c))

                    # --- ZONE APERÇU (Ajustée pour la nouvelle taille) ---
                    with ui.element('div').classes('w-full flex-grow bg-black/10 rounded-lg p-3 overflow-hidden text-sm text-white/90').style('margin-bottom: 55px;'):
                        events = cal.get('events', {})
                        if events:
                            ui.label('Prochains événements :').classes('font-semibold mb-2 underline')
                            compteur = 0
                            for date, liste_ev in sorted(events.items()):
                                if compteur >= 3: # Maintenant on peut afficher 3 événements grâce à la carte plus grande !
                                    break
                                for ev in liste_ev:
                                    if compteur < 3:
                                        try:
                                            date_formatee = "/".join(date.split('-')[1:][::-1])
                                        except:
                                            date_formatee = date
                                        ui.label(f'{date_formatee} : {ev}').classes('truncate')
                                        compteur += 1
                        else:
                            with ui.column().classes('w-full h-full items-center justify-center opacity-40 gap-2'):
                                ui.icon('calendar_today', size='lg')
                                ui.label('Aucun événement').classes('text-xs')

                    # Ton bouton "Ouvrir" ajusté pour la nouvelle hauteur (top: 88%)
                    ui.button("Ouvrir", on_click=lambda cid=cal['id']: ui.navigate.to(f'/calendrier/{cid}')).style(
                        f'position: absolute; transform: translate(-50%, -50%); top: 88%; left: 50%; width: 80%; height: 14%; border-radius: 50px; {police1}'
                    ).classes('text-xl font-bold')
        # --- EN DESSOUS DE TES PROPRES CALENDRIERS ---
    from Database import get_calendriers_partages
    
    partages = get_calendriers_partages(user_id)
    if partages:
        ui.label('Calendriers partagés avec moi').style(f'{Layout.police3}; color: {Layout.couleurtexte1}').classes('text-2xl font-bold mt-8 mb-2')
        with ui.row().classes('w-full gap-4'):
            for p in partages:
                cal_p = p['cal']
                proprio = p['owner_name']
                droit = p['permission']
                
                with ui.card().classes('w-64 p-4 cursor-pointer hover:scale-105 transition-transform').style(f'background-color: {Layout.fondsecondaire}; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1)'):
                    ui.label(cal_p['name']).classes('text-xl font-bold').on('click', lambda cid=cal_p['id']: ui.navigate.to(f'/calendrier/{cid}'))
                    ui.label(f"Par : {proprio}").classes('text-xs opacity-70')
                    couleur_badge = 'orange' if droit == 'Lecture' else 'green'
                    ui.badge(droit, color=couleur_badge).classes('text-2xs self-start mt-2')

    def generer_snapshot(name: str) -> str:
        jours = ['L', 'M', 'M', 'J', 'V', 'S', 'D']
        
        header = ''.join(
            f'<div style="background: {violetfoncé}; color: {blanc}; text-align: center; font-size: 10px; padding: 2px; order-radius: 2px">{j}</div>'
            for j in jours
        )
        days = ''.join(
            f'<div style="background: {violet}; color: {blanc}; text-align: center; font-size: 10px; padding: 2px; border-radius: 2px">{i}</div>'
            for i in range(1, 32)
        )
        
        cell = f'background: {violetfoncé}; color: {blanc}; text-align: center; font-size: 10px; padding: 2px; border-radius: 2px'
        grid_style = 'display: grid; grid-template-columns: repeat(7,1fr); gap: 2px; margin-bottom: 6px'
        
        return (
            f'<div style="margin: 0; padding: 8px; background: {rosemoyen}; font-family: sans-serif; overflow: hidden; height: 100%">'
            f'<div style="font-weight: bold; font-size: 14px; color: {violetsombre}; margin-bottom: 6px">Aperçu</div>'
            f'<div style="{grid_style}">{header}{days}</div>'
            f'<div style="color: {violetsombre}; font-size: 10px; font-style: italic">Aucun évènement</div>'
            f'</div>'
        )
        
    def ajouter_calendrier():

        calendriers = get_calendriers()

        new_cal = {
            'id': str(uuid.uuid4()),
            'name': f'Calendrier {len(calendriers) + 1}',
            'snapshot': '',
            'events': {}
        }

        calendriers.append(new_cal)

        save_user_calendars(user_id, calendriers)

        liste_calendriers.refresh()

    def boite_renommer(cal_id):
        calendriers = get_calendriers()
        cal = next(c for c in calendriers if c['id'] == cal_id) # <-- NOUVEAU CODE PROPRE
        with ui.dialog() as dialog, ui.card():
            ui.label('Renommer le calendrier').classes('font-bold text-xl')
            nom_entrée = ui.input('Nouveau nom', value=cal['name'])
            with ui.row():
                ui.button('Annuler', on_click=dialog.close)
                def save_name():
                    cal['name'] = nom_entrée.value
                    save_user_calendars(user_id, calendriers)
                    dialog.close()
                    liste_calendriers.refresh()
                ui.button('Sauvegarder', on_click=save_name).style(f'background-color: {violetfoncé}; color: white')
        dialog.open()

    def supprimer_calendrier(cal_id):

        calendriers = [
            c for c in get_calendriers()
            if c['id'] != cal_id
        ]

        save_user_calendars(user_id, calendriers)

        liste_calendriers.refresh()

    mes_calendriers = get_calendriers() 

    accueildesign("Accueil", 125, len(mes_calendriers), on_add=ajouter_calendrier)
    
    liste_calendriers()

