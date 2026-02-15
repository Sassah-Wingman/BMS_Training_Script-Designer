import PySimpleGUI as sg

import Script_Images
import Script_Functions
import module2

alignleft = sg.TEXT_LOCATION_LEFT

def start_window():
    installed_bms = Script_Functions.get_list_of_BMS()
    start_tooltips = ["Start a new training script.", 
                     "Edit an existed training script.", 
                     "Exit application.", 
                     "List of installed BMS versions."]
    
    title_top = [[sg.Text("Welcome to BMS Training Script Designer.", font = "_ 22")],]
   
    left_col = sg.Column([[sg.Text(" ", text_color = "#ffffff", background_color = "#64778d")],
                          #fake button
                          [sg.Button(button_text = " ", 
                                     button_color= "#64778d", 
                                     size = (24, 2), 
                                     enable_events = False, 
                                     border_width = 0,
                                     disabled = True)],
                          [sg.Button(button_text = "Create Script", 
                                     key = "-CREATES-", 
                                     size = (16, 2), 
                                     font = "_ 16",
                                     tooltip = start_tooltips[0])],
                          [sg.Text(" ", background_color = "#64778d")],
                          [sg.Button(button_text = "Edit Script",
                                     key = "-EDITS-", 
                                     size = (16, 2), 
                                     font = "_ 16",
                                     tooltip = start_tooltips[1])],
                          [sg.Text(" ", background_color = "#64778d")],
                          [sg.Button(button_text = "EXIT", 
                                     key = "-EXITS-", 
                                     size = (16, 2), 
                                     font = "_ 14",
                                     tooltip = start_tooltips[2])],
                          [sg.Text(" ", background_color = "#64778d")],           
                          [sg.Text(text = "Hi folks!\n\nFalcon BMS includes the ability to create interactive training missions.  This is accomplished by means of training scripts which are simple text files (either with a .txt or a .run extension) that are loaded with the training mission and contain the interactive training instructions.\nA simple text editor can be used to manipulate these scripts.\nHowever, an API would be an easier way to assist users to fulfill this task.\nWe really hope that this tool helps users to take advantage of this amazing BMS tool.", 
                                     text_color= "#000000", 
                                     background_color = "#91a6be",
                                     font = "arial 11",
                                     size = (26, 19), 
                                     enable_events = False, 
                                     border_width = 0, 
                                     justification = "left")],
                          [sg.Text(" ", background_color = "#64778d")],
                          [sg.Button(button_text = "Quick Guide",
                                     key = "-TUTO-",
                                     size = (14, 1),
                                     font = "_ 11",
                                     tooltip = start_tooltips[1])],
                                     [sg.Text(" ", background_color = "#64778d")],], 
                           background_color = "#64778d", element_justification = "center" ,vertical_alignment = "top")
                          
    right_col = sg.Column([[sg.Graph((1291, 727), (0,0), (1291, 727), background_color='white', key = "-graph-")],
                           [sg.HorizontalSeparator()],
                           [sg.Text("Select the Falcon BMS version you want to work with: "),
                           sg.Combo(values = installed_bms, 
                           setting = sg.user_settings_get_entry(key = "-setbms-"),
                           size = (30,1), 
                           enable_events=True,
                           readonly = True,
                           tooltip = start_tooltips[3],
                           key = "-BMS-")],
                           [sg.Text("Falcon BMS Campaign path: ", 
                                    font = "_ 14"), 
                                    sg.Text(sg.user_settings_get_entry("-setcamp-"),
                                    text_color = "#ffffff", 
                                    key = "=camp=")],
                           [sg.HorizontalSeparator()]],
                           vertical_alignment = "top") 

    layout = [[title_top], [left_col, right_col]]

    start_window = sg.Window("BMS Training Script Designer.", 
                            layout, 
                            icon = Script_Images.start_icon, 
                            return_keyboard_events = False, 
                            finalize=True, 
                            resizable=True,
                            location = (150, 50), 
                            size = (1650, 900))
    
    #update widgets over image
    start_window["-graph-"].draw_image(data = Script_Images.start_image, location = (0, 727))
    start_window["-graph-"].draw_rectangle((240,10), (1040, 150), fill_color = "#d4d7dd", line_color = "#B9BBBE")
    start_window["-graph-"].draw_text("Falcon BMS versions detected:", (600, 140), font = "_ 14", color = "#000000")
    
    #update wigets with list of installed versions of BMS
    axis_x = 600
    axis_y = 110
    for path_ in Script_Functions.get_installed_BMS_path().values():
        print(">>win/start - BMS path: ", path_)
        start_window["-graph-"].draw_text(text = path_, location = (axis_x, axis_y), font = "_ 16", color = "#64778d")
        axis_y = axis_y - 30

    while True:
        event, values = start_window.read()
        print(">>WIN/START - events: ", event)
        
        if event in (sg.WIN_CLOSED, "-EXITS-"):
            print(">>win/start - event: exit")
            break
                   
        if event == "-BMS-":
            #Choose BMS version and enable creation/edition
            sg.user_settings_set_entry("-setbms-", values["-BMS-"])
            print(">>win/start - bms version: ", values["-BMS-"])
            #Display campaign folder path
            data_path = values["-BMS-"] + "\\Data\Campaign"
            sg.user_settings_set_entry("-setcamp-", data_path)
            print(">>win/start - campaign folder: ", data_path)
            start_window["=camp="].update(data_path)
            start_window.refresh()
            
        if event == "-CREATES-":
            module2.create_window()
        
        if event == "-EDITS-":
            pass

         
    start_window.close()  
    return start_window



