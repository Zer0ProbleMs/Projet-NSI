from nicegui import app, ui
import Layout as L
from Database import get_amis

# Partie ou tout est stocké dans les serveurs nicegui

def _conv_key(user_a: str, user_b: str) -> str:
    return "conv__" + "__".join(sorted([user_a, user_b]))

def get_messages(user_a: str, user_b: str) -> list:
    return app.storage.general.get(_conv_key(user_a, user_b), [])

def send_message(sender: str, receiver: str, text: str):
    key = _conv_key(sender, receiver)
    msgs = app.storage.general.get(key, [])
    msgs.append({"from": sender, "text": text})
    app.storage.general[key] = msgs

def last_message(user_a: str, user_b: str) -> str:
    msgs = get_messages(user_a, user_b)
    if not msgs:
        return "Aucun message"
    m = msgs[-1]
    preview = m['text'][:28] + "…" if len(m['text']) > 28 else m['text']
    return f"{m['from']}: {preview}"

# Partie menu de la messagerie

def messagerie():
    from Database import load_config

    user_id = app.storage.user.get('user_id', 'user_0')

    config = load_config()

    # vrai pseudo connecté
    moi = config[user_id].get('username', 'Invité') \
        if user_id in config else 'Invité'

    amis_ids = get_amis(user_id)

    # convertir les IDs en pseudos
    amis = [
        config[uid].get('username', uid)
        for uid in amis_ids
        if uid in config
    ]

    with ui.menu().style(
        f'transform: translate(-50%, -50%); '
        f'width: 280px; max-height: 380px; overflow-y: auto; '
        f'background-color: {L.couleurcontour}; border-radius: 14px; '
        f'box-shadow: 0 8px 32px #0008; padding: 0;'
    ) as menu:

        # En-tête
        with ui.row().classes('items-center justify-between w-full').style(
            f'background-color: {L.fondsecondaire}; padding: 8px 12px; '
            f'border-radius: 14px 14px 0 0; flex-shrink: 0;'
        ):
            ui.label(f'💬  {moi}').style(
                f'color: {L.couleurtexte1}; font-size: .95rem; {L.police3}'
            )
            ui.icon('close', size='1.3rem').style(
                f'color: {L.couleurtexte1}; cursor: pointer; opacity: 0.7'
            ).on('click', menu.close)

        ui.separator().style(f'background-color: {L.couleurbouton}; margin: 0')

        if not amis:
            ui.label("Aucun ami pour l'instant.").style(
                f'color: {L.couleurtexte2}; font-style: italic; '
                f'padding: 14px; font-size: .82rem; {L.police5}'
            )
        else:
            for ami in amis:
                apercu = last_message(moi, ami)
                with ui.row().classes('items-center w-full cursor-pointer').style(
                    f'padding: 8px 12px; border-bottom: 1px solid {L.couleurbouton}; '
                    f'transition: opacity .15s;'
                ).on('click', lambda a=ami, m=menu, me=moi: [m.close(), _ouvrir_conversation(me, a)]):
                    # Avatar initiale
                    ui.label(ami[0].upper()).style(
                        f'min-width: 36px; height: 36px; border-radius: 50%; '
                        f'background: {L.couleurbouton}; color: {L.couleurtexte2}; '
                        f'font-size: 1rem; display: flex; align-items: center; '
                        f'justify-content: center; flex-shrink: 0; {L.police4}'
                    )
                    with ui.column().classes('gap-0').style(
                        'margin-left: 8px; min-width: 0; overflow: hidden'
                    ):
                        ui.label(ami).style(
                            f'color: {L.couleurtexte2}; font-weight: 600; '
                            f'{L.police5}; font-size: .88rem'
                        )
                        ui.label(apercu).style(
                            f'color: {L.couleurtexte2}; font-size: .70rem; opacity: 0.65; '
                            f'white-space: nowrap; overflow: hidden; '
                            f'text-overflow: ellipsis; max-width: 175px'
                        )

# Partie de l'envoie des messages

def _ouvrir_conversation(moi: str, ami: str):
    with ui.dialog().props('persistent') as conv_dialog, \
         ui.card().style(
            f'width: 340px; height: 350px; '
            f'background-color: {L.couleurcontour}; border-radius: 14px; '
            f'box-shadow: 0 8px 32px #0008; padding: 0; '
            f'display: flex; flex-direction: column; overflow: hidden;'
         ):

        # En-tête
        with ui.row().classes('items-center justify-between w-full').style(
            f'background-color: {L.fondsecondaire}; padding: 8px 12px; '
            f'flex-shrink: 0; border-radius: 14px 14px 0 0;'
        ):
            with ui.row().classes('items-center gap-2'):
                ui.label(ami[0].upper()).style(
                    f'width: 30px; height: 30px; border-radius: 50%; '
                    f'background: {L.couleurbouton}; color: {L.couleurtexte2}; '
                    f'font-size: .9rem; display: flex; align-items: center; '
                    f'justify-content: center; {L.police4}'
                )
                ui.label(ami).style(
                    f'color: {L.couleurtexte1}; font-size: .95rem; '
                    f'font-weight: 700; {L.police5}'
                )
            ui.icon('close', size='1.2rem').style(
                f'color: {L.couleurtexte1}; cursor: pointer; opacity: 0.7'
            ).on('click', conv_dialog.close)

        # Zone messages (flex: 1 pour prendre l'espace restant)
        with ui.scroll_area().style(
            f'flex: 1; padding: 8px; background-color: {L.couleurcontour}; '
            f'min-height: 0;'
        ):
            messages_col = ui.column().classes('w-full').style('gap: 5px')

            @ui.refreshable
            def afficher_messages():
                messages_col.clear()
                with messages_col:
                    msgs = get_messages(moi, ami)
                    if not msgs:
                        ui.label("Commencez la conversation !").style(
                            f'color: {L.couleurtexte2}; opacity: 0.6; font-style: italic; '
                            f'text-align: center; margin-top: 16px; '
                            f'font-size: .78rem; width: 100%'
                        )
                    for msg in msgs:
                        est_moi = (msg['from'] == moi)
                        with ui.row().classes('w-full').style(
                            f'justify-content: {"flex-end" if est_moi else "flex-start"}'
                        ):
                            ui.label(msg['text']).style(
                                f'max-width: 200px; padding: 6px 10px; '
                                f'border-radius: {"12px 12px 2px 12px" if est_moi else "12px 12px 12px 2px"}; '
                                f'background: {L.couleurbouton if est_moi else L.fondsecondaire}; '
                                f'color: {L.couleurtexte2 if est_moi else L.couleurtexte2}; '
                                f'font-size: .82rem; word-break: break-word; {L.police5}'
                            )

            afficher_messages()
            ui.timer(2.0, afficher_messages.refresh)

        # Zone saisie
        with ui.row().classes('items-center w-full').style(
            f'padding: 6px 10px; background-color: {L.fondsecondaire}; '
            f'flex-shrink: 0; gap: 6px; border-radius: 0 0 14px 14px;'
        ):
            champ = ui.input(placeholder='Message…').style(
                f'flex: 1; font-size: .82rem;'
            ).props('dense outlined rounded dark')

            def envoyer():
                texte = champ.value.strip()
                if texte:
                    send_message(moi, ami, texte)
                    champ.set_value('')
                    afficher_messages.refresh()

            ui.icon('send', size='1.5rem').style(
                f'color: {L.couleurbouton}; cursor: pointer; filter: brightness(1.3);'
            ).on('click', envoyer)
            champ.on('keydown.enter', envoyer)

    conv_dialog.open()
