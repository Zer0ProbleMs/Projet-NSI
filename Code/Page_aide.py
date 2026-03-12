from nicegui import *
from Layout import *

@ui.page('/aide')
def aide():
    layout()
    maindesign("Aide", 300)
    ui.label("This is the standing title").classes('text-4xl font-bold font-italic text-center')
    ui.separator()
    ui.label("Here you are on our website. How  are we supposed to help you if we don't even know where to start?").classes('text-2xl font-light')
    ui.label("> Well here, this page is our very working page, a page that's looking to help you through our site").classes('text-2xl font-light')

    
ui.run()