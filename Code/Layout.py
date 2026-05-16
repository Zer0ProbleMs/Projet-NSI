from nicegui import app, ui
from Database import *
from Login import *
from Page_Messagerie import messagerie
from Page_Messagerie import _ouvrir_conversation
import Page_Messagerie as pm

bgrose = '<style>body {background-color: #d7a0d7;}</style>'
bgvertsombre = '<style>body {background-color: #244237;}</style>'
bgblanc2 = '<style>body {background-color: #f0dbdb;}</style>'

violetsombre = '#3d0070'; violetfoncé = '#8030c0'; violetmoyen = '#9037d0'; violet = '#964be1'; rosemoyen = '#d293d2'; rose = '#d7a0d7'; roseclair = '#eeccee' # Thème Violet / Rose
vertsombre = '#244237'; vertfoncé = '#285a48'; vert = '#408a71'; vertclair = '#b0e4cc'
blanc2 = '#f0dbdb'; beigeclair = '#f5d6d6'; rosetrèsclair = '#F9DFDF'; rose2 = '#F5AFAF'
jaune = '#ffd600' 
blanc = '#ffffff'; noir = '#000000' # Couleur de texte 

police1 = 'font-family: Iosevka Charon' # Différentes polices d'écritures importé
police2 = 'font-family: Oswald'
police3 = 'font-family: Bebas Neue'
police4 = 'font-family: Bungee'
police5 = 'font-family: Fredoka'

theme_sombre = 'Violet'

fond = bgrose
fondsecondaire = rosemoyen
couleurcontour = violetfoncé
couleurbouton = violet
couleurlogo = rose
couleurcontourlogo = violet
couleurcalendrier = rosemoyen
couleurtexte1 = noir
couleurtexte2 = blanc


def layout():
    ui.add_head_html(fond)
    ui.colors(primary=couleurbouton)
    ui.add_head_html('''<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Bungee&family=Fredoka:wght@300..700&family=Iosevka+Charon:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&family=Oswald:wght@200..700&display=swap" rel="stylesheet">''') # Charge la police d'écriture "Barrio"

def musique_de_fond():   
    bgmusique = ui.audio('Musique/Walk in the Forest v2.mp3', autoplay=False, controls=False, loop=True)
    with ui.knob(color='orange', track_color='grey', center_color='white', size='4rem',min=0, max=1, step=0.05, value=1, on_change=lambda e: ui.run_javascript(f'document.querySelector("audio").volume = {e.value}')).style(f'position: absolute; left: 50%; top: 45%; transform: translate(-50%, -50%)').props('push glossy'):
        ui.icon('volume_up')
    ui.button(on_click=lambda: bgmusique.props('muted'), icon='volume_off').style(f'position: absolute; left: 50%; top: 65%; transform: translate(-50%, -50%)').props('push glossy size=1.5rem')
    ui.button(on_click=lambda: bgmusique.props(remove='muted'), icon='volume_up').style(f'position: absolute; left: 50%; top: 55%; transform: translate(-50%, -50%)').props('push glossy size=1.5rem')

def maindesign(nomdepage, largeurg):
    ui.page_title(nomdepage)
    layout()
    with ui.header(elevated=True).style(f'background-color: {couleurcontour}; height: 10%').classes('items-center justify-between') as header: # La partie couleurprimairete en haut
        ui.label(nomdepage).style(f'{police4}; position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl text-left underline')
        friendcirclelogo("47")
        ui.input(placeholder='Rechercher...').style(f'position: absolute; left: 65%; top: 20%; width: 30%; background-color: {couleurbouton}; border-radius: 5px').classes('text-xl')
        
        with ui.button(on_click= lambda: ui.navigate.to('/profile')).props('push glossy').style('border-radius: 50px; transform: translate(-50%, -50%); width: 4.25%; top: 35%; left: 104%'):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')

    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurcontour}; width: 50%').props(f'width={largeurg}') as left_drawer: # La partie couleurprimairete à gauche
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 75px; box-shadow: none; border-radius: 15px').props('push glossy'):
                menus()
                    
        with ui.button(on_click= lambda: ui.navigate.to('/aidegénéral')).props('push glossy').style('position: absolute; border-radius: 25px; transform: translate(-50%, -50%); width: 75%; top: 95%; left: 50%'):
            ui.icon("help").props('size=4rem').style(f'color: {couleurcontour}')

    with ui.right_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurcontour}; width: 50%').props('width=125') as right_drawer:
        with ui.row().classes('w-full items-center').style(f'-webkit-text-stroke: 3px {couleurbouton}'):
            
            # Notifications
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').props('size=5rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style(f'background-color: {couleurbouton}; color: white').classes('text-2xl py-5 px-25 text-center font-light')

            # Chat
            with ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').props('size=5rem'):
                messagerie()

            # Contacts
            with ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').props('size=5rem'):
                menu_amis()

        musique_de_fond()


            
            
    footer = ui.footer().style(f'background-color: {couleurcontour}') # La partie couleurprimaire en bas

def accueildesign(nomdepage, largeurg, ncal, on_add=None):
    ui.page_title(nomdepage)
    layout()   

    with ui.header(elevated=True).style(f'background-color: {couleurcontour}; height: 10%').classes('items-center justify-between'):
        ui.label(nomdepage).style(f'{police4}; position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl text-left underline') 
        friendcirclelogo("47")
        ui.input(placeholder='Rechercher...').style(f'position: absolute; left: 65%; top: 20%; width: 30%; background-color: {couleurbouton}; border-radius: 5px').classes('text-xl')
        
        with ui.button(on_click= lambda: ui.navigate.to('/profile')).props('push glossy').style('border-radius: 50px; transform: translate(-50%, -50%); width: 4.25%; top: 35%; left: 104%'):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurcontour}; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 75px; box-shadow: none; border-radius: 15px').props('push glossy'):
                menus()
        with ui.button(on_click= lambda: ui.navigate.to('/aidegénéral')).props('push glossy').style('position: absolute; border-radius: 25px; transform: translate(-50%, -50%); width: 75%; top: 95%; left: 50%'):
            ui.icon("help").props('size=4rem').style(f'color: {couleurcontour}')
            
    with ui.right_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurcontour}; width: 50%').props('width=125') as right_drawer:
        with ui.row().classes('w-full items-center').style(f'-webkit-text-stroke: 3px {couleurbouton}'):
            
            # Notifications
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').props('size=5rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style(f'background-color: {couleurbouton}; color: white').classes('text-2xl py-5 px-25 text-center font-light')

            # Chat
            with ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').props('size=5rem'):
                messagerie()

            # Contacts
            with ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').props('size=5rem'):
                menu_amis()

        musique_de_fond()

    ui.footer().style(f'background-color: {couleurcontour}')         

def designaide(nomdepage, largeurg):
    ui.page_title(nomdepage)
    layout()   

    with ui.header(elevated=True).style(f'background-color: {couleurcontour}; height: 10%').classes('items-center justify-between'):
        ui.label(nomdepage).style(f'{police4}; position: absolute; top: 50%; left: 5%; transform: translate(-50%, -50%);').classes('text-4xl text-left underline')
        friendcirclelogo("45")
        ui.input(placeholder='Rechercher...').style(f'position: absolute; left: 65%; top: 20%; width: 30%; background-color: {couleurbouton}; border-radius: 5px').classes('text-xl')
        
        with ui.button(on_click= lambda: ui.navigate.to('/profile')).props('push glossy').style('border-radius: 50px; transform: translate(-50%, -50%); width: 4.75%; top: 35%; left: 104%'):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')

    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurcontour}; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; height: 100px; box-shadow: none; border-radius: 15px').props('push glossy'):
                menus()
        
        listeaides()   
        with ui.button(on_click= lambda: ui.navigate.to('/aidegénéral')).props('push glossy').style('position: absolute; border-radius: 25px; transform: translate(-50%, -50%); width: 75%; top: 95%; left: 50%'):
            ui.icon("help").props('size=4rem').style(f'color: {couleurcontour}')

    with ui.right_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurcontour}; width: 50%').props('width=125') as right_drawer:
        with ui.row().classes('w-full items-center').style(f'-webkit-text-stroke: 3px {couleurbouton}'):
            
            # Notifications
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').props('size=5rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style(f'background-color: {couleurbouton}; color: white').classes('text-2xl py-5 px-25 text-center font-light')

            # Chat
            with ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').props('size=5rem'):
                messagerie()

            # Contacts
            with ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').props('size=5rem'):
                menu_amis()

        musique_de_fond()

            #Les boutons notifications et messages se trouverons la!

    ui.footer().style(f'background-color: {couleurcontour}')

def menus():
    user_id = app.storage.user.get('user_id', '')
    config = load_config()
    pseudo = config[user_id].get('username', 'Utilisateur') if user_id and user_id in config else 'Utilisateur'
    
    with ui.menu().style(f'background-color: {couleurbouton}; {police2}; color: white; border-radius: 10px') as menu:
        ui.label(pseudo).classes('text-2xl py-5 px-25 text-center text-medium')
        ui.separator().style(f'background-color: {fondsecondaire}')
        ui.menu_item('Paramètres', on_click=lambda: ui.navigate.to('/parametres')).classes('text-2xl py-5 px-25 text-center font-light')
        ui.separator().style(f'background-color: {fondsecondaire}')
        ui.menu_item('Fermer', menu.close).classes('text-2xl py-5 px-25 text-center font-light')

def menu_amis():
    from Database import load_config, get_all_user_ids
    
    config = load_config()
    
    # Récupère tous les users sauf soi-même
    mon_id = app.storage.user.get('user_id', '')
    amis = [(uid, config[uid].get('username', '?')) for uid in get_all_user_ids() if uid != mon_id]
    noms = [nom for _, nom in amis]

    with ui.menu().style('transform: translate(-30%, 65%); width: 20%') as menu:
        ui.label("Amis").style(f'background-color: {couleurcontour}; color: white; {police3}').classes('text-3xl py-5 px-25 text-center font-light')
        ui.separator().style(f'background-color: {couleurcontour}')
        ui.input(placeholder='Rechercher...', autocomplete=noms).style(f'width: 100%; background-color: {couleurcontour}; {police5}')
        
        for uid, nom in amis:
            with ui.slide_item().style(f'background-color: {fondsecondaire}; color: {couleurtexte2}; border-radius: 3px; width: 100%; height: 100%') as slide_item:
                with ui.item(on_click=lambda u=uid: ui.navigate.to(f'/profil/{u}')):  # ← clique → profil
                    with ui.item_section().props('avatar'):
                        ui.icon('person')
                    with ui.item_section():
                        ui.item_label(nom).style(f'{police5}')
                with slide_item.right():
                    with ui.item(on_click=slide_item.reset):
                        ui.item_section('Supprimer?')
                        with ui.item_section().props('avatar'):
                            ui.icon('delete')

def menu_amis():
    from Database import load_config, get_all_user_ids
    
    config = load_config()
    
    # Récupère tous les users sauf soi-même
    mon_id = app.storage.user.get('user_id', '')
    mon_nom = config[mon_id].get('username', 'Invité')
    amis = [(uid, config[uid].get('username', '?')) for uid in get_all_user_ids() if uid != mon_id]
    noms = [nom for _, nom in amis]

    with ui.menu().style(f'transform: translate(-50%, -50%); width: 20%; max-height: 380px; overflow-y: auto; background-color: {couleurcontour}; border-radius: 14px; box-shadow: 0 8px 32px #0008; padding: 0;') as menu:
        ui.label("Amis").style(f'background-color: {fondsecondaire}; color: white; {police3}').classes('text-3xl py-5 px-25 text-center font-light')
        ui.separator().style(f'background-color: {couleurcontour}')
        ui.input(placeholder='Rechercher...', autocomplete=noms).style(f'width: 100%; background-color: {couleurcontour}; {police5}')
        
        for uid, nom in amis:
            with ui.slide_item().style(f'background-color: {couleurcontour}; color: {couleurtexte2}; border-radius: 3px; width: 100%; height: 100%') as slide_item:
                with ui.item(on_click=lambda u=uid: ui.navigate.to(f'/profil/{u}')):  # ← clique → profil
                    with ui.card().style(f'background: #c084fc22; border: 1px solid {couleurcontour}; padding: 16px 20px; width: 100%; cursor: pointer;'):
                        with ui.row().classes('items-center gap-4 w-full'):
                            ui.label(nom[0]).style(f'width: 46px; height: 46px; border-radius: 50%; background: {couleurcontour}; color: {couleurtexte2}; font-size: 18px; display: flex; align-items: center; justify-content: center')
                            with ui.column().classes('gap-0'):
                                ui.label(nom).style(f'font-weight: 500; color: {couleurtexte2}; {police5}')
                                ui.label('En ligne').style(f'font-size: 12px; color: {fondsecondaire}')
                            ui.element('div').style('width: 8px; height: 8px; border-radius: 50%; background: #22c55e; margin-left: auto')
                            
                    with slide_item.right(): # Permet de faire glisser l'item vers la gauche et y afficher des options
                        with ui.row().classes():
                            with ui.item(on_click=slide_item.reset): # La partie pour retourner en arrière
                                with ui.item_section().props('avatar'):
                                    ui.icon('arrow_back_ios')
                                ui.item_section('Annuler').style('transform: translate(-50%, 0%)')
                            with ui.item(on_click=slide_item.delete): # Permet de supprimer une des bulles
                                ui.item_section('Supprimer?').style('transform: translate(35%, 0%)')
                                with ui.item_section().props('avatar'):
                                    ui.icon('delete')
                                    
                    with slide_item.left(): # Permet de faire glisser l'item vers la droite et y afficher des options
                        with ui.row().classes():
                            with ui.item(on_click=lambda ami=nom: _ouvrir_conversation(mon_nom, ami)):
                                ui.item_section('Envoyer Message').style('transform: translate(20%, 0%)') # Permet de renvoyer l'utilisateur au menu message
                                with ui.item_section().props('avatar'):
                                    ui.icon('sms')
                            with ui.item(on_click=slide_item.reset): # La partie pour retourner en arrière
                                with ui.item_section().props('avatar'):
                                    ui.icon('arrow_back_ios')
                                ui.item_section('Annuler').style('transform: translate(-50%, 0%)')

                            

                                
def listeaides():
    with ui.scroll_area().classes('w-65 h-full'):
        with ui.column().classes('w-full h-full').style(f"transform: translate(-5%); {police3}"):
            with ui.expansion(text='Aides Principales', group='group').style(f'color: white; background-color: {couleurbouton}; border-radius: 5px').classes('w-full text-xl font-light'):
                ui.label('- Général').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/aidegénéral'))
                ui.label('- Profile').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/aideprofile'))  
            with ui.expansion(text='Notre Parcours', group='group').style(f'color: white; background-color: {couleurbouton}; border-radius: 5px').classes('w-full text-xl font-light'):
                ui.label('- Qui sommes nous?').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/quinoussommes'))
                ui.label('- Le départ').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/départ'))
            with ui.expansion(text='Easter Egg', group='group').style(f'color: white; background-color: {couleurbouton}; border-radius: 5px').classes('w-full text-xl font-light'):
                ui.label('- Poème').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/eastereggpoème'))

def friendcirclelogo(gauche):

    with ui.label("FRIEND").style(f'{police4}; color: {couleurlogo}; position: absolute; top: 10%; left: {gauche}%; letter-spacing: -8px; -webkit-text-stroke: 2px {couleurcontourlogo}').classes('text-7xl cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to(target='/')):
        ui.label("CIRCLE").style(f'{police3}; color: {couleurlogo}; position: absolute; left: 60%; top: 60%; letter-spacing: 1px; -webkit-text-stroke: 1px {couleurcontourlogo}').classes('text-4xl text-bold')
        ui.label("+").style(f'{police4}; color: {jaune}; position: absolute; left: 92%; top: 52%; letter-spacing: 1px; -webkit-text-stroke: 1px {couleurcontourlogo}').classes('text-5xl text-bold')
        
def login():
    global username
    global password
    with ui.dialog() as dialog, ui.card():
        ui.label('Se connecter').classes('font-bold text-xl')
        username = ui.input('Pseudonyme')
        password = ui.input('Mot de passe')
        with ui.row():
            ui.button('Annuler', on_click=dialog.close)
            def sauvegarder():
                dialog.close()
            ui.button('Sauvegarder', on_click=sauvegarder).style(f'background-color: {violetfoncé}; color: white')
    dialog.open()
