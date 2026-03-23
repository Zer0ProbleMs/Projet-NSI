from nicegui import app, ui
bgbleumerfoncé = '<style>body {background-color: #1a1a2e;}</style>'
bgrose = '<style>body {background-color: #d7a0d7;}</style>'
bgvertsombre = '<style>body {background-color: #091413;}</style>'

violettrèsfoncé = '#3d0070'; violetfoncé = '#8030c0'; violetmoyen = '#9037d0'; violet = '#964be1'; rosemoyen = '#d293d2'; rose = '#d7a0d7'; roseclair = '#eeccee' # Thème Violet / Rose
bleumerfoncé = '#1a1a2e'; bleumer = '#02343f'; bleufoncé = '#16213e'; bleucyan = '#0f3460'; rouge = '#e94560' # Thème Bleu / Rouge
vertsombre = '#091413'; vertfoncé = '#285a48'; vert = '#408a71'; vertclair = '#b0e4cc'
jaune = '#ffd600' 
blanc = '#ffffff'; noir = '#000000' # Couleur de texte 

police1 = 'font-family: Iosevka Charon' # Différentes polices d'écritures importé
police2 = 'font-family: Oswald'
police3 = 'font-family: Bebas Neue'
police4 = 'font-family: Bungee'
police5 = 'font-family: Fredoka'

theme_sombre = 'violet'
bgact = bgrose
c1act = violet
c2act = violetfoncé
t1act = rose
ctexte = noir

def layout(couleurbg, couleursecondaire):
    ui.add_head_html(couleurbg)
    ui.colors(primary=couleursecondaire)
    ui.add_head_html('''<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Bungee&family=Fredoka:wght@300..700&family=Iosevka+Charon:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&family=Oswald:wght@200..700&display=swap" rel="stylesheet">''') # Charge la police d'écriture "Barrio"

def maindesign(nomdepage, largeurg, couleurbg, couleurprimaire, couleursecondaire, teint):
    ui.page_title(nomdepage)
    layout(couleurbg, couleursecondaire)   
    global header, footer, left_drawer, right_drawer
    with ui.header(elevated=True).style(f'background-color: {couleurprimaire}; height: 10%').classes('items-center justify-between') as header: # La partie couleurprimairete en haut
        ui.label(nomdepage).style(f'{police4}; position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl text-left underline')
        friendcirclelogo("47", couleursecondaire, teint)
        ui.input(placeholder='Rechercher...').style(f'position: absolute; left: 65%; top: 20%; width: 30%; background-color: {couleursecondaire}; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 101.7%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')

    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurprimaire}; width: 50%').props(f'width={largeurg}') as left_drawer: # La partie couleurprimairete à gauche
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 75px; box-shadow: none; border-radius: 15px'):
                menus(couleurbg, couleurprimaire, couleursecondaire, teint)
                    
        with ui.avatar().style('position: absolute; left: 30%; top: 93%').classes('w-12 h-12 cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/aidegénéral')):
            ui.icon("help").props('size=3rem').style(f'color: {couleurprimaire}')

    with ui.right_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurprimaire}; width: 50%').props('width=125') as right_drawer: # La partie couleurprimairete à droite
        #Les boutons notifications et messages se trouverons la! 
        with ui.row().classes('w-full items-center').style(f'-webkit-text-stroke: 3px {couleursecondaire}'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').on('click', lambda: ui.notify("You pressed the notification button")).props('size=5rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style(f'background-color: {couleursecondaire}; color: white').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').on('click', lambda: ui.notify("You pressed the messages button")).props('size=5rem')
            ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').on('click', lambda: menu_amis(couleurbg, couleurprimaire, couleursecondaire)).props('size=5rem')
      
    footer = ui.footer().style(f'background-color: {couleurprimaire}') # La partie couleurprimaire en bas
    return header, footer, left_drawer, right_drawer

def accueildesign(nomdepage, largeurg, couleurbg, couleurprimaire, couleursecondaire, teint, ncal, on_add=None):
    ui.page_title(nomdepage)
    layout(couleurbg, couleursecondaire)   

    with ui.header(elevated=True).style(f'background-color: {couleurprimaire}; height: 10%').classes('items-center justify-between'):
        ui.label(nomdepage).style(f'{police4}; position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl text-left underline') 
        friendcirclelogo("47", couleursecondaire, teint)
        ui.input(placeholder='Rechercher...').style(f'position: absolute; left: 65%; top: 20%; width: 30%; background-color: {couleursecondaire}; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 101.7%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurprimaire}; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 75px; box-shadow: none; border-radius: 15px'):
                menus(couleurbg, couleurprimaire, couleursecondaire, teint)
        with ui.avatar().style('position: absolute; left: 30%; top: 93%').classes('w-12 h-12 cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/aidegénéral')):
            ui.icon("help").props('size=3rem').style(f'color: {couleurprimaire}')

    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: {couleurprimaire}; width: 50%').props('width=125'):
        with ui.avatar().style('position: absolute; left: 25%; top: 92%').classes('w-15 h-15 cursor-pointer hover:opacity-80').on('click', lambda e: on_add() if on_add else ui.notify("Aucune action définie")):
            ui.icon('add_circle').style(f'position: absolute; transform: translate(-50%, -50%); top: 50%; left: 50%; width: 50%; color: {teint}').props('size=4rem')
            
        with ui.row().classes('w-full items-center'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white; -webkit-text-stroke: 3px {couleursecondaire}').on('click', lambda: ui.notify("You pressed the notification button")).props('size=5rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style(f'background-color: {couleursecondaire}; color: white').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white; -webkit-text-stroke: 3px {couleursecondaire}').on('click', lambda: ui.notify("You pressed the messages button")).props('size=5rem')
            ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white; -webkit-text-stroke: 3px {couleursecondaire}').on('click', lambda: menu_amis(couleurbg, couleurprimaire, couleursecondaire)).props('size=5rem')

    ui.footer().style(f'background-color: {couleurprimaire}')         

def designaide(nomdepage, largeurg, couleurbg, couleurprimaire, couleursecondaire, teint):
    ui.page_title(nomdepage)
    layout(couleurbg, couleursecondaire)   

    with ui.header(elevated=True).style(f'background-color: {couleurprimaire}; height: 10%').classes('items-center justify-between'):
        ui.label(nomdepage).style(f'{police4}; position: absolute; top: 50%; left: 5%; transform: translate(-50%, -50%);').classes('text-4xl text-left underline')
        friendcirclelogo("45", couleursecondaire, teint)
        ui.input(placeholder='Rechercher...').style(f'position: absolute; left: 65%; top: 20%; width: 30%; background-color: {couleursecondaire}; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 101.7%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
            
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: {couleurprimaire}; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; height: 100px; box-shadow: none; border-radius: 15px'):
                menus(couleurbg, couleurprimaire, couleursecondaire, teint)
        
        listeaides(couleurbg, couleurprimaire, couleursecondaire)   
                
        with ui.avatar().style('position: absolute; left: 40%; top: 93%').classes('w-12 h-12 cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/aidegénéral')):
            ui.icon("help").props('size=3rem').style(f'color: {couleurprimaire}')

    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: {couleurprimaire}; width: 50%').props('width=125'):
        with ui.row().classes('w-full items-center'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white; -webkit-text-stroke: 3px {couleursecondaire}').on('click', lambda: ui.notify("You pressed the notification button")).props('size=5rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style(f'background-color: {couleursecondaire}; color: white').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white; -webkit-text-stroke: 3px {couleursecondaire}').on('click', lambda: ui.notify("You pressed the messages button")).props('size=5rem')
            ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white; -webkit-text-stroke: 3px {couleursecondaire}').on('click', lambda: menu_amis(couleurbg, couleurprimaire, couleursecondaire)).props('size=5rem')

            #Les boutons notifications et messages se trouverons la!

    ui.footer().style(f'background-color: {couleurprimaire}')

def menus(couleurbg, couleurprimaire, couleursecondaire, teint): # Une fonction qui permet le bon fonctionnement du bouton menu qui se situe dans le coin en haut à gauche
    with ui.menu().style(f'background-color: {couleursecondaire}; {police2}; color: white; border-radius: 10px') as menu:
        ui.label(" Friend Circle +").classes('text-2xl py-5 px-25 text-center text-medium underline')
        ui.separator().style(f'background-color: {teint}')
        ui.menu_item('Paramètres', on_click=lambda: ui.navigate.to('/paramètres')).classes('text-2xl py-5 px-25 text-center font-light')
        ui.separator().style(f'background-color: {teint}')
        ui.menu_item('Fermer', menu.close).classes('text-2xl py-5 px-25 text-center font-light')

def menu_amis(couleurbg, couleurprimaire, couleursecondaire): # Une fonction qui permet le bon fonctionnement du bouton contacts
        with ui.menu().style('transform: translate(-30%, 65%); width: 20%') as menu:
            ui.label("Amis").style(f'background-color: {couleurprimaire}; color: white; {police3}').classes('text-3xl py-5 px-25 text-center font-light')
            ui.separator().style(f'background-color: {couleurprimaire}')
            amis = ["Daris", "Tidianne", "Anfel", "Cat"]
            ui.input(placeholder='Rechercher...', autocomplete=amis).style(f'width: 100%; background-color: {couleurprimaire}; {police5}')
            for ami in amis:
                with ui.row().classes('items-center gap-2 p-2').style(f'background-color: {couleursecondaire}'):
                    with ui.slide_item().style(f'background-color: {rose}; border-radius: 3px; width: 100%; height: 100%') as slide_item:
                        with ui.item():
                            with ui.item_section().props('avatar'):
                                ui.icon('person')
                            with ui.item_section():
                                ui.item_label(ami).style(f'{police5}')
                            with slide_item.right():
                                with ui.item(on_click=slide_item.reset):
                                    ui.item_section('Supprimer?')
                                    with ui.item_section().props('avatar'):
                                        ui.icon('delete')

def listeaides(couleurbg, couleurprimaire, couleursecondaire):
    with ui.scroll_area().classes('w-65 h-full'):
        with ui.column().classes('w-full h-full').style(f"transform: translate(-5%); {police3}"):
            with ui.expansion(text='Aides Principales', group='group').style(f'color: white; background-color: {couleursecondaire}; border-radius: 5px').classes('w-full text-xl font-light'):
                ui.label('- Général').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/aidegénéral'))
                ui.label('- Profile').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/aideprofile'))  
            with ui.expansion(text='Notre Parcours', group='group').style(f'color: white; background-color: {couleursecondaire}; border-radius: 5px').classes('w-full text-xl font-light'):
                ui.label('- Qui sommes nous?').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/quinoussommes'))
                ui.label('- Le départ').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/départ'))
            with ui.expansion(text='Easter Egg', group='group').style(f'color: white; background-color: {couleursecondaire}; border-radius: 5px').classes('w-full text-xl font-light'):
                ui.label('- Poème').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/eastereggpoème'))

def friendcirclelogo(gauche, couleursecondaire, teint):

    with ui.label("FRIEND").style(f'{police4}; color: {teint}; position: absolute; top: 10%; left: {gauche}%; letter-spacing: -8px; -webkit-text-stroke: 2px {couleursecondaire}').classes('text-7xl cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to(target='/')):
        ui.label("CIRCLE").style(f'{police3}; color: {teint}; position: absolute; left: 60%; top: 60%; letter-spacing: 1px; -webkit-text-stroke: 1px {couleursecondaire}').classes('text-4xl text-bold')
        ui.label("+").style(f'{police4}; color: {jaune}; position: absolute; left: 92%; top: 52%; letter-spacing: 1px; -webkit-text-stroke: 1px {couleursecondaire}').classes('text-5xl text-bold')