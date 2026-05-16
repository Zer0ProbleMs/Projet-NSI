from nicegui import app, ui
from Layout import *
from Database import verify_login

@ui.page('/login')
def login_page():
    layout()  # ← applique le fond et les polices

    def try_login():
        user_id = verify_login(username.value, password.value)
        if user_id:
            app.storage.user['user_id'] = user_id
            ui.navigate.to('/')
        else:
            ui.notify('Identifiants incorrects', color='negative')

    with ui.card().classes('absolute-center').style(
        f'background-color: {fondsecondaire}; '
        f'border-radius: 15px; '
        f'box-shadow: 0px 0px 20px {couleurcontour}; '
        f'padding: 3rem; '
        f'width: 400px; '
        f'min-height: 350px;'
    ):
        friendcirclelogo("35")  # ← logo en haut
        ui.label('Connexion').style(
            f'color: {couleurtexte1}; {police4}'
        ).classes('text-3xl font-bold mt-16')
        username = ui.input('Pseudo').style(
            f'background-color: {couleurbouton}; border-radius: 8px; width: 100%'
        )
        password = ui.input('Mot de passe', password=True).style(
            f'background-color: {couleurbouton}; border-radius: 8px; width: 100%'
        )
        ui.button('Se connecter', on_click=try_login).style(
            f'width: 100%; border-radius: 50px; margin-top: 1rem'
        ).props('push glossy')

@ui.page('/logout')
def logout():
    app.storage.user.clear()
    ui.navigate.to('/login')