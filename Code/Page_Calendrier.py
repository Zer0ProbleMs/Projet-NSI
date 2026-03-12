from nicegui import ui
from Layout import *

@ui.page('/calendrier')
def Calendrier():
    maindesign("Calendrier", 100)
    
ui.run()