from nicegui import app, ui

navyblue = '#02343f'
beige = '#f0edcc'
rose = '#d7a0d7'
violetfoncé = '#8030c0'
violettrèsfoncé = ''
violetmoyen = '#9037d0'
violet = '#964be1'

def layout():
    ui.add_head_html('<style>body {background-color: #d7a0d7;}</style>')
    ui.colors(primary='#8030c0')

def maindesign(nomdepage, largeurg):
    ui.page_title(nomdepage)
    layout()   

    ui.footer().style(f'background-color: #964be1') # La partie violette en bas
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: #964be1; width: 50%').props(f'width={largeurg}'): # La partie violette à gauche
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 75px; box-shadow: none; border-radius: 10px'):
                menus()
                    
        with ui.avatar().style('position: absolute; left: 30%; top: 93%').classes('w-12 h-12 cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/aidegénéral')):
            ui.icon("help").props('size=3rem').style(f'color: {violet}')

    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: #964be1; width: 50%').props('width=125'): # La partie violette à droite
        #Les boutons notifications et messages se trouverons la!
        with ui.row().classes('w-full items-center'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').on('click', lambda: ui.notify("You pressed the notification button")).props('size=4rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').on('click', lambda: ui.notify("You pressed the messages button")).props('size=4rem')
            ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').on('click', lambda: menu_amis()).props('size=4rem')

    with ui.header(elevated=True).style(f'background-color: #964be1; height: 10%').classes('items-center justify-between'): # La partie violette en haut
        with ui.link(target='/'):
            ui.image('Designs/FriendCircle1.png').classes('w-64').style('position: absolute; top: 50%; left: 55%; transform: translate(-50%, -50%);')
        ui.input(placeholder='Rechercher...').style('position: absolute; left: 65%; top: 20%; width: 30%; background-color: #8030c0; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 101.7%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
        ui.label(nomdepage).style('position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl font-extrabold text-left')      

def accueildesign(nomdepage, largeurg, ncal, on_add=None):
    ui.page_title(nomdepage)
    layout()   

    ui.footer().style(f'background-color: #964be1')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: #964be1; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 75px; box-shadow: none; border-radius: 10px'):
                menus()
        with ui.avatar().style('position: absolute; left: 30%; top: 93%').classes('w-12 h-12 cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/aidegénéral')):
            ui.icon("help").props('size=3rem').style(f'color: {violet}')
    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: #964be1; width: 50%').props('width=125'):
        with ui.avatar().style('position: absolute; left: 26%; top: 91%').classes('w-15 h-15 cursor-pointer hover:opacity-80').on('click', lambda e: on_add() if on_add else ui.notify("Aucune action définie")):
            ui.icon('add_circle').style(f'position: absolute; transform: translate(-50%, -50%); top: 50%; left: 51%; width: 50%; color: {rose}').props('size=4rem')
        #Les boutons notifications et messages se trouverons la!
        with ui.row().classes('w-full items-center'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').on('click', lambda: ui.notify("You pressed the notification button")).props('size=4rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').on('click', lambda: ui.notify("You pressed the messages button")).props('size=4rem')
            ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').on('click', lambda: menu_amis()).props('size=4rem')


    with ui.header(elevated=True).style(f'background-color: #964be1; height: 10%').classes('items-center justify-between'):
        with ui.link(target='/'):
            ui.image('Designs/FriendCircle1.png').classes('w-64').style('position: absolute; top: 50%; left: 55%; transform: translate(-50%, -50%);')
        ui.input(placeholder='Rechercher...').style('position: absolute; left: 65%; top: 20%; width: 30%; background-color: #8030c0; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 101.7%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
        ui.label(nomdepage).style('position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl font-extrabold text-left')      

def designaide(nomdepage, largeurg):
    ui.page_title(nomdepage)
    layout()   

    ui.footer().style(f'background-color: #964be1')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: #964be1; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%; height: 100px; box-shadow: none; border-radius: 10px'):
                menus()
                
        with ui.scroll_area().classes('w-70 h-full'):
            with ui.column().classes('w-full h-full').style("transform: translate(-5%)"):
                with ui.expansion(text='Aides Principales', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px').classes('w-full text-xl font-light'):
                    ui.label('- Général').style(f'background-color: {violetmoyen}; border-radius: 5px').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/aidegénéral'))
                    ui.label('- Profile').style(f'background-color: {violetmoyen}; border-radius: 5px').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/aideprofile'))  
                with ui.expansion(text='Notre Parcours', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px').classes('w-full text-xl font-light'):
                    ui.label('- Qui sommes nous?').style(f'background-color: {violetmoyen}; border-radius: 5px;').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/quinoussommes'))
                    ui.label('- Le départ').style(f'background-color: {violetmoyen}; border-radius: 5px;').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/départ'))
                with ui.expansion(text='Easter Egg', group='group').style(f'color: #ffffff; background-color: {violetmoyen}; border-radius: 5px').classes('w-full text-xl font-light'):
                    ui.label('- Poème').style(f'background-color: {violetmoyen}; border-radius: 5px').classes('cursor-pointer hover:opacity-80 px-2').on('click', lambda: ui.navigate.to('/eastereggpoème'))
                
        with ui.avatar().style('position: absolute; left: 40%; top: 93%').classes('w-12 h-12 cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/aidegénéral')):
            ui.icon("help").props('size=3rem').style(f'color: {violet}')

    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: #964be1; width: 50%').props('width=125'):
        with ui.row().classes('w-full items-center'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15%; color: white').on('click', lambda: ui.notify("You pressed the notification button")).props('size=4rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%; color: white').on('click', lambda: ui.notify("You pressed the messages button")).props('size=4rem')
            ui.icon('contacts').classes('w-16 cursor-pointer hover:opacity-80').style(f'position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%; color: white').on('click', lambda: menu_amis()).props('size=4rem')

            #Les boutons notifications et messages se trouverons la!

    with ui.header(elevated=True).style(f'background-color: #964be1; height: 10%').classes('items-center justify-between'):
        with ui.link(target='/'):
            ui.image('Designs/FriendCircle1.png').classes('w-64').style('position: absolute; top: 50%; left: 55%; transform: translate(-50%, -50%);')
        ui.input(placeholder='Rechercher...').style('position: absolute; left: 65%; top: 20%; width: 30%; background-color: #8030c0; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 101.7%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
        ui.label(nomdepage).style('position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl font-extrabold text-left')

def menus(): # Une fonction qui permet le bon fonctionnement du bouton menu qui se situe dans le coin en haut à gauche
    with ui.menu() as menu:
        ui.label(" Friend Circle +").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-underline')
        ui.separator().style(f'background-color: {violetmoyen}')
        ui.menu_item('Paramètres', on_click=lambda: ui.navigate.to('/paramètres')).style(f'background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light')
        ui.separator().style(f'background-color: {violetmoyen}')
        ui.menu_item('Fermer', menu.close).props('dense').style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light')

def menu_amis(): # Une fonction qui permet le bon fonctionnement du bouton contacts
        with ui.menu().style('transform: translate(-30%, 65%); width: 20%') as menu:
            ui.label("Amis").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light')
            ui.separator().style('background-color: #964be1')
            amis = ["Daris", "Tidianne", "Anfel", "Cat"]
            ui.input(placeholder='Rechercher...', autocomplete=amis).style('width: 100%; background-color: #964be1')
            for ami in amis:
                with ui.row().classes('items-center gap-2 p-2').style('background-color: #8030c0'):
                    with ui.slide_item().style('background-color: #d7a0d7; border-radius: 3px; width: 100%; height: 100%') as slide_item:
                        with ui.item():
                            with ui.item_section().props('avatar'):
                                ui.icon('person')
                            with ui.item_section():
                                ui.item_label(ami)
                            with slide_item.right():
                                with ui.item(on_click=slide_item.reset):
                                    ui.item_section('Supprimer?')
                                    with ui.item_section().props('avatar'):
                                        ui.icon('delete')

