from nicegui import app, ui
from Friend_Circle_Main import *
from Page_aide import *
from Page_paramètres import *
from Page_Profil import *
from Page_Calendrier import *
from Modification import*

def pages():
    ui.sub_pages({'/': Main_page, '/paramètres': Paramètres, '/aide': Aide, '/profile': Profile, '/calendrier': Calendrier, '/modification' : Modification})