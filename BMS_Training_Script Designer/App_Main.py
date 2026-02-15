# The purpose of this application is to design training scripts for Falcon BMS.
# Framework: FreeSimpleGUI
# project start: jul 2024
#__version__ = "1.4 - sep 2025"

# colors (ligthest to darkest):
#d4d7dd: light gray    
#91a6be: naval light blue
#64778d: naval dark blue
#4b586e: lead dark gray

#Framework PySimpleGUI
import FreeSimpleGUI as sg

#My modules
import App_Open_Window    #module to start the application

#global configurations
__version__ = "v1.4 - 2025."
sg.set_options(font = "Arial, 10")
BMSBlueGray = {'BACKGROUND': '#91a6be',
             "TEXT": "#000000",
             "INPUT": "#ffffff",
             "TEXT_INPUT": "#000000",
             "SCROLL": "#64778d",
             "BUTTON": ("#ffffff", "#4b586e"),
             "PROGRESS": ("#64778d", "#d4d7dd"),
             "BORDER": 2, 
             "SLIDER_DEPTH": 0, 
             "PROGRESS_DEPTH": 0}
sg.theme_add_new("BMSBlueGray", BMSBlueGray)
sg.theme("BMSBlueGray")

#program entry point
def main():
    App_Open_Window.open_window()
    
if __name__ == "__main__":    
    main()        
