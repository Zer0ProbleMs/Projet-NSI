from nicegui import app, ui

navyblue = '#02343f'
beige = '#f0edcc'
rose = '#d7a0d7'
violetfoncé = '#8030c0'
violet = '#964be1'

def layout():
    ui.add_head_html('<style>body {background-color: #d7a0d7;}</style>')
    ui.colors(primary='#8030c0')

def maindesign(nomdepage, largeurg):
    ui.page_title(nomdepage)
    layout()   

    ui.footer().style(f'background-color: #964be1')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: #964be1; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('position: absolute; top: 5%; left: 50%; transform: translate(-50%, -50%); width: 99%; height: 10%; box-shadow: none; border-radius: 10px'):
                with ui.menu() as menu:
                    ui.label("FriendCircle+").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light')
                    ui.separator().style('background-color: #8030c0')
                    ui.menu_item('Paramètres', on_click=lambda: ui.navigate.to('/paramètres')).style(f'background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-left font-light')
                    ui.separator().style('background-color: #8030c0')
                    ui.menu_item('Fermer', menu.close).props('dense').style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-left font-light')
        with ui.link(target='/aide'):
            ui.image("Designs/Point_d'interrogation.png").classes('w-16').style('position: absolute; top: 90%; left: 22%')

    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: #964be1; width: 50%').props('width=125'):
        #Les boutons notifications et messages se trouverons la!
        with ui.row().classes('w-full items-center'):
            with ui.image('Designs/Cloche.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15% ').on('click', lambda e: ui.notify("You pressed the notification button")):
                with ui.menu() as menu:
                    ui.label("Hello").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.image('Designs/Message_icon.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%').on('click', lambda e: ui.notify("You pressed the messages button"))
            ui.image('Designs/Friends_icon.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%').on('click', lambda e: ui.notify("You pressed the friends button"))

    with ui.header(elevated=True).style(f'background-color: #964be1; height: 10%').classes('items-center justify-between'):
        with ui.link(target='/'):
            ui.image('Designs/FriendCircle1.png').classes('w-64').style('position: absolute; top: 50%; left: 55%; transform: translate(-50%, -50%);')
        ui.input(placeholder='Rechercher...').style('position: absolute; left: 65%; top: 20%; width: 30%; background-color: #8030c0; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 102%;').classes('w-16 h-16'):
            with ui.link(target='/profile'):
                ui.image('Designs/Profil_icon.png').classes('w-24')
        ui.label(nomdepage).style('position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl font-extrabold text-left')      

def accueildesign(nomdepage, largeurg, ncal, on_add=None):
    ui.page_title(nomdepage)
    layout()   

    ui.footer().style(f'background-color: #964be1')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: #964be1; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('position: absolute; top: 5%; left: 50%; transform: translate(-50%, -50%); width: 99%; height: 10%; box-shadow: none; border-radius: 10px'):
                menus()
        with ui.link(target='/aide'):
            ui.image("Designs/Point_d'interrogation.png").classes('w-16').style('position: absolute; top: 90%; left: 22%')
    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: #964be1; width: 50%').props('width=125'):
        with ui.button(on_click=lambda e: on_add() if on_add else ui.notify("Aucune action définie")).style('position: absolute; transform: translate(-50%, -50%); top: 95%; left: 50%; width: 100%; height: 15%'):
            ui.icon('add_circle').style('position: absolute; transform: translate(-50%, -50%); top: 43%; left: 50%; width: 50%').props('size=4rem')
        #Les boutons notifications et messages se trouverons la!
        with ui.row().classes('w-full items-center'):
            with ui.icon('notifications').classes('cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15% ').on('click', lambda: ui.notify("You pressed the notification button")).props('size=4rem'):
                with ui.menu() as menu:
                    ui.label("Hello").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.icon('chat').classes('cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%').on('click', lambda: ui.notify("You pressed the messages button")).props('size=4rem')
            ui.image('Designs/Friends_icon.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 35%').on('click', lambda: menu_amis())


    with ui.header(elevated=True).style(f'background-color: #964be1; height: 10%').classes('items-center justify-between'):
        with ui.link(target='/'):
            ui.image('Designs/FriendCircle1.png').classes('w-64').style('position: absolute; top: 50%; left: 55%; transform: translate(-50%, -50%);')
        ui.input(placeholder='Rechercher...').style('position: absolute; left: 65%; top: 20%; width: 30%; background-color: #8030c0; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 102%;').classes('w-16 h-16').classes('cursor-pointer hover:opacity-80').on('click', lambda: ui.navigate.to('/profile')):
            ui.icon('account_circle').props('size=4rem').props('size=4rem')
        ui.label(nomdepage).style('position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl font-extrabold text-left')      

def designaide(nomdepage, largeurg):
    ui.page_title(nomdepage)
    layout()   

    ui.footer().style(f'background-color: #964be1')
    
    with ui.left_drawer(top_corner=True, bottom_corner=True, elevated=True).style(f'background-color: #964be1; width: 50%').props(f'width={largeurg}'):
        with ui.row().classes('w-full items-center'):
            with ui.button(icon='menu').style('position: absolute; top: 5%; left: 50%; transform: translate(-50%, -50%); width: 99%; height: 10%; box-shadow: none; border-radius: 10px'):
                menus()
        with ui.tabs().style('position: absolute; top: 10%; left: 50%; transform: translate(-50%, -100%); width: 30%; height: 40%').props('vertical').classes('w-full') as tabs:
            mail = ui.tab('Mails')
            alarm = ui.tab('Alarms')    
            movie = ui.tab('Movies')
            
        with ui.link(target='/aide'):
            ui.image("Designs/Point_d'interrogation.png").classes('w-16').style('position: absolute; top: 90%; left: 22%')

    with ui.right_drawer(top_corner=True, bottom_corner=True).style(f'background-color: #964be1; width: 50%').props('width=125'):
        with ui.button().style('position: absolute; transform: translate(-50%, -50%); top: 95%; left: 50%; width: 100%; height: 15%'):
            ui.image('Designs/Symbole_plus2.png').style('position: absolute; transform: translate(-50%, -50%); top: 43%; left: 50%').classes('w-16')
        with ui.row().classes('w-full items-center'):
            with ui.image('Designs/Cloche.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 15% ').on('click', lambda e: ui.notify("You pressed the notification button")):
                with ui.menu() as menu:
                    ui.label("Hello").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light') # A remplacer par une petite boîte page qui affiche les notifications d'utilisateurs
            ui.image('Designs/Message_icon.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%').on('click', lambda e: ui.notify("You pressed the messages button"))
            ui.image('Designs/Message_icon.png').classes('w-16 cursor-pointer hover:opacity-80').style('position: absolute; transform: translate(-50%, -50%); left: 50%; top: 25%').on('click', lambda e: ui.notify("You pressed the friends button")) 

            #Les boutons notifications et messages se trouverons la!

    with ui.header(elevated=True).style(f'background-color: #964be1; height: 10%').classes('items-center justify-between'):
        with ui.link(target='/'):
            ui.image('Designs/FriendCircle1.png').classes('w-64').style('position: absolute; top: 50%; left: 55%; transform: translate(-50%, -50%);')
        ui.input(placeholder='Rechercher...').style('position: absolute; left: 65%; top: 20%; width: 30%; background-color: #8030c0; border-radius: 5px').classes('text-xl')
        
        with ui.avatar().style('position: absolute; left: 102%;').classes('w-16 h-16'):
            with ui.link(target='/profile'):
                ui.image('Designs/Profil_icon.png').classes('w-24')
        ui.label(nomdepage).style('position: absolute; top: 50%; left: 10%; transform: translate(-50%, -50%);').classes('text-4xl font-extrabold text-left')

def menus():
    with ui.menu() as menu:
        ui.label("FriendCircle+").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light')
        ui.separator().style('background-color: #8030c0')
        ui.menu_item('Paramètres', on_click=lambda: ui.navigate.to('/paramètres')).style(f'background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-left font-light')
        ui.separator().style('background-color: #8030c0')
        ui.menu_item('Fermer', menu.close).props('dense').style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-left font-light')

def menu_amis():
        with ui.menu() as menu:
            ui.label("Amis").style('background-color: #8030c0; color: #ffffff').classes('text-2xl py-5 px-25 text-center font-light')
            ui.separator().style('background-color: #964be1')
            amis = ["Daris", "Tidianne", "Quelqu'un"]
            ui.input(placeholder='Rechercher...', autocomplete=amis).style('width: 100%; background-color: #8030c0')
            for ami in amis:
                with ui.row().classes('items-center gap-2 p-2').style('background-color: #8030c0') :
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
                    ui.separator()