#Framework PySimpleGUI
import FreeSimpleGUI as sg

#My modules
import App_Images       #module with images used in the application
import App_Functions    #module with functions to get BMS paths and other utilities
import App_Workspace_Window    #module with windows used in the application 

alignleft = sg.TEXT_LOCATION_LEFT

def open_window():
    ListOfInstalledBMS = App_Functions.get_list_of_bms_path()
    ListOfBMSPath = sg.user_settings_get_entry(key = "-setbmspath-") 
    start_tooltips = ["Start using the application.", "Exit application.", "List of installed BMS versions."]
    
    title_top = [[sg.Text("Welcome to BMS Training Script Designer.", font = "_ 22"), sg.Push(), sg.Text("ver 1.4 - sep/25. Copyright 2024, FreeSimpleGUI.")],]
   
    left_col = sg.Column([[sg.Text(" ", text_color = "#ffffff", background_color = "#64778d")],
                          #fake button 1
                          [sg.Button(button_text = " ", 
                                     button_color= "#64778d", 
                                     size = (24, 2), 
                                     enable_events = False, 
                                     border_width = 0,
                                     disabled = True)],
                          [sg.Button(button_text = "ENTER", 
                                     key = "-ENTER_SCPT-", 
                                     size = (16, 2), 
                                     font = "_ 16",
                                     disabled = False,
                                     tooltip = start_tooltips[0])],
                          #fake button 2
                          [sg.Button(button_text = " ", 
                                     button_color= "#64778d", 
                                     size = (24, 14), 
                                     enable_events = False, 
                                     border_width = 0,
                                     disabled = True)],
                          [sg.Button(button_text = "EXIT", 
                                     key = "-EXIT_SCPT-", 
                                     size = (12, 2), 
                                     font = "_ 14",
                                     tooltip = start_tooltips[1])],
                          [sg.Text(" ", background_color = "#64778d")],           
                          [sg.Text(" ", background_color = "#64778d")],           
                          [sg.Text(text = "Hi folks!\n\nFalcon BMS includes the ability to create interactive training missions.  This is accomplished by means of training scripts which are simple text files (either with a .txt or a .run extension) that are loaded with the training mission and contain the interactive training instructions.\nA simple text editor can be used to manipulate these scripts.\nHowever, an API would be an easier way to assist users to fulfill this task.\nWe really hope that this tool helps users to take advantage of this amazing BMS tool.", 
                                   text_color= "#000000", 
                                   background_color = "#91a6be",
                                   font = "arial 11",
                                   size = (26, 19), 
                                   enable_events = False, 
                                   border_width = 0, 
                                   justification = "left")],
                          [sg.Text(" ", background_color = "#64778d")],], 
                          background_color = "#64778d", element_justification = "center" ,vertical_alignment = "top")

    right_col = sg.Column([[sg.Graph((1291, 727), (0,0), (1291, 727), background_color='white', key = "-graph-")], #1291, 727
                           [sg.HorizontalSeparator()],
                           [sg.Text("Select the Falcon BMS version you want to work with: "),
                            sg.Combo(values = ListOfInstalledBMS, 
                                     default_value = ListOfBMSPath,
                                     size = (30,1), 
                                     enable_events=True,
                                     readonly = True,
                                     tooltip = start_tooltips[2],
                                     key = "-BMS_VER-")],
                           [sg.Text("Falcon BMS Campaign path: ", 
                                    font = "_ 14"), 
                                    sg.Text(sg.user_settings_get_entry("-setcamppath-"),
                                    text_color = "#ffffff", 
                                    key = "-CAMP_FOLD-")],
                           [sg.Text("Falcon BMS Callbacks path: ", 
                                    font = "_ 14"), 
                                    sg.Text(sg.user_settings_get_entry("-setcallbackpath-"),
                                    text_color = "#ffffff", 
                                    key = "-CALLBACK_FOLD-")],
                           [sg.Text("Falcon BMS F16 Manuals path: ", 
                                    font = "_ 14"), 
                                    sg.Text(sg.user_settings_get_entry("-setmanualpath-"),
                                    text_color = "#ffffff", 
                                    key = "-MANUAL_FOLD-")],],
                           vertical_alignment = "top") 

    layout = [[title_top], [left_col, right_col]]

    open_window = sg.Window("BMS Training Script Designer.", 
                             layout, 
                             icon = App_Images.start_icon, 
                             return_keyboard_events = False, 
                             finalize=True, 
                             resizable=True,
                             location = (150, 50), 
                             size = (1650, 950))    
    
    #update widgets over image
    open_window["-graph-"].draw_image(data = App_Images.start_image, location = (0, 727))
    open_window["-graph-"].draw_rectangle((240,10), (1040, 150), fill_color = "#d4d7dd", line_color = "#B9BBBE")
    open_window["-graph-"].draw_text("Falcon BMS versions detected:", (600, 140), font = "_ 14", color = "#000000")
    
    #update wigets with list of installed versions of BMS
    axis_x = 600 
    axis_y = 110 
    for path_ in App_Functions.get_list_of_installed_bms_path().values():
        print(">>win/start - BMS path: ", path_)
        open_window["-graph-"].draw_text(text = path_, location = (axis_x, axis_y), font = "_ 16", color = "#64778d")
        axis_y = axis_y - 30
   
    while True:
        event, values = open_window.read()
        print(">>WIN/START - events: ", event)

        if event in (sg.WIN_CLOSED, "-EXIT_SCPT-"):
            print(">>win/start - event: exit")
            break
                   
        #Choose BMS version and set campaign and docs path
        if event == "-BMS_VER-":
            sg.user_settings_set_entry("-setbmspath-", values["-BMS_VER-"])
            print(">>win/start - bms version: ", values["-BMS_VER-"])
            #Display campaign folder path
            data_path = values["-BMS_VER-"] + r"\Data\Campaign"
            callback_path = values["-BMS_VER-"] + r"\Docs\01 Input Devices\02 Key File Editor"
            manual_path = values["-BMS_VER-"] + r"\Docs\02 Aircraft Manuals & Checklists\01 F-16"
            sg.user_settings_set_entry("-setcamppath-", data_path)
            sg.user_settings_set_entry("-setcallbackpath-", callback_path)
            sg.user_settings_set_entry("-setmanualpath-", manual_path)
            open_window["-CAMP_FOLD-"].update(data_path)
            open_window["-CALLBACK_FOLD-"].update(callback_path)
            open_window["-MANUAL_FOLD-"].update(manual_path)
            open_window["-ENTER_SCPT-"].update(disabled = False)
            print(">>win/start - campaign folder: ", data_path)
            print(">>win/start - callback folder: ", callback_path)
            print(">>win/start - f16manual folder: ", manual_path)
            open_window.refresh()
        
        # Check BMS selection and open manager window   
        if event == "-ENTER_SCPT-":
            if not values["-BMS_VER-"]:
                sg.popup_ok("Please select a valid Falcon BMS version.", font = "_ 14", no_titlebar = True, modal = True, keep_on_top = True)
            else:
                App_Workspace_Window.workspace_window()
                print(">>win/start - Manage Window.")
         
    open_window.close()  
    return open_window



