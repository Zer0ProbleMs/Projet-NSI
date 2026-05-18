from nicegui import app, ui
from Layout import *
import Layout
from Database import verify_login

@ui.page('/login')
def login_page():
    Layout.layout()  # ← applique le fond et les polices

    def try_login():
        user_id = verify_login(username.value, password.value)
        if user_id:
            app.storage.user['user_id'] = user_id
            ui.navigate.to('/')
        else:
            ui.notify('Identifiants incorrects', color='negative')

    with ui.card().classes('absolute-center').style(f'background-color: {Layout.fondsecondaire}; border-radius: 15px; box-shadow: 0px 0px 20px {Layout.couleurcontour}; padding: 3rem; width: 400px; min-height: 350px;'):
        Layout.friendcirclelogo("17.5")  # ← logo en haut
        ui.label('Connexion').style( f'color: {Layout.couleurtexte1}; {Layout.police4}').classes('text-3xl font-bold mt-16')
        username = ui.input('Pseudo').style(f'background-color: {Layout.couleurbouton}; border-radius: 8px; width: 100%')
        password = ui.input('Mot de passe', password=True, password_toggle_button=True).style(f'background-color: {Layout.couleurbouton}; border-radius: 8px; width: 100%')
        ui.button('Se connecter', on_click=try_login).style(f'width: 100%; border-radius: 50px; margin-top: 1rem').props('push glossy')

@ui.page('/logout')
def logout():
    app.storage.user.clear()
    ui.navigate.to('/login')