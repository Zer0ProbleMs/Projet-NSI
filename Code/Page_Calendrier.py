from nicegui import ui, app
from Layout import *
import Layout

from Database import get_user_calendars, save_user_calendars

import calendar
from datetime import datetime

@ui.page('/calendrier/{cal_id}')
def Page_Calendrier(cal_id: str):

    user_id = app.storage.user.get('user_id')

    if not user_id:
        ui.navigate.to('/login')
        return

    calendriers = get_user_calendars(user_id)

    cal = next((c for c in calendriers if c['id'] == cal_id), None)

    if cal is None:
        ui.label('Calendrier introuvable').classes('text-red-500 text-2xl')
        ui.button(
            'Retour',
            on_click=lambda: ui.navigate.to('/')
        )
        return

    maindesign(cal['name'], 125)

    if 'events' not in cal:
        cal['events'] = {}

    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year

    mois_fr = [
        '',
        'Janvier',
        'Février',
        'Mars',
        'Avril',
        'Mai',
        'Juin',
        'Juillet',
        'Août',
        'Septembre',
        'Octobre',
        'Novembre',
        'Décembre'
    ]

    jours_fr = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']

    calendar.setfirstweekday(calendar.MONDAY)

    with ui.column().classes('w-full items-center'):

        with ui.row().classes('items-center gap-10 mt-5'):
            ui.button(
                icon='arrow_back',
                on_click=lambda: changer_mois(-1)
            ).props('round')

            titre = ui.label().classes('text-4xl font-bold')

            ui.button(
                icon='arrow_forward',
                on_click=lambda: changer_mois(1)
            ).props('round')

        grille = ui.column().classes('w-full items-center')
    
    def sauvegarder():
        save_user_calendars(user_id, calendriers)

    def supprimer_event(date_key, index):
        if date_key in cal['events']:
            cal['events'][date_key].pop(index)

            if len(cal['events'][date_key]) == 0:
                del cal['events'][date_key]

            sauvegarder()
            afficher_calendrier()

    def ouvrir_jour(date_key):
        with ui.dialog() as dialog, ui.card().style(
            f'background-color: {Layout.fondsecondaire}; width: 500px'
        ):

            ui.label(f'Évènements du {date_key}').classes(
                'text-2xl font-bold'
            )

            events = cal['events'].get(date_key, [])

            if events:
                for i, ev in enumerate(events):
                    with ui.card().classes('w-full'):
                        ui.label(ev).classes('text-lg')

                        ui.button(
                            'Supprimer',
                            on_click=lambda idx=i: (
                                supprimer_event(date_key, idx),
                                dialog.close()
                            )
                        ).props('flat color=red')
            else:
                ui.label('Aucun évènement')

            nouvelle_entree = ui.input('Nouvel évènement').classes('w-full')

            def ajouter_evenement():
                texte = nouvelle_entree.value.strip()

                if not texte:
                    return

                if date_key not in cal['events']:
                    cal['events'][date_key] = []

                cal['events'][date_key].append(texte)

                sauvegarder()

                dialog.close()
                afficher_calendrier()

            with ui.row():
                ui.button('Fermer', on_click=dialog.close)

                ui.button(
                    'Ajouter',
                    on_click=ajouter_evenement
                ).style(
                    f'background-color: {Layout.violetfoncé}; color: white'
                )

        dialog.open()
    
    @ui.refreshable
    def afficher_calendrier():

        titre.set_text(f'{mois_fr[current_month]} {current_year}')

        grille.clear()

        with grille:

            with ui.grid(columns=7).classes('gap-2 w-full p-5'):

                for jour in jours_fr:
                    with ui.card().classes('p-2 text-center font-bold').style(
                        f'background-color: {Layout.violetfoncé}; '
                        f'color: white; '
                        f'border-radius: 10px'
                    ):
                        ui.label(jour).classes('text-lg text-center')

                month_days = calendar.monthcalendar(current_year, current_month)

                for week in month_days:
                    for day in week:

                        if day == 0:
                            ui.element('div').classes('h-32')
                            continue

                        date_key = f'{current_year}-{current_month:02d}-{day:02d}'

                        events = cal['events'].get(date_key, [])

                        couleur = Layout.roseclair

                        if len(events) > 0:
                            couleur = Layout.violet

                        with ui.card().classes(
                            'w-full h-32 cursor-pointer'
                        ).style(
                            f'background-color: {couleur}; '
                            f'border-radius: 15px; '
                            f'overflow: hidden'
                        ).on(
                            'click',
                            lambda d=date_key: ouvrir_jour(d)
                        ):

                            ui.label(str(day)).classes(
                                'text-xl font-bold'
                            )

                            for ev in events[:3]:
                                ui.label(f'• {ev}').classes(
                                    'text-sm'
                                )

                            if len(events) > 3:
                                ui.label('...').classes('text-sm')
                
    def changer_mois(direction):
        nonlocal current_month, current_year

        current_month += direction

        if current_month < 1:
            current_month = 12
            current_year -= 1

        if current_month > 12:
            current_month = 1
            current_year += 1

        afficher_calendrier.refresh()

    afficher_calendrier()