import FreeSimpleGUI as sg

import App_Images
import App_Functions
import App_Manual
import App_Popups_Window
import App_Tree
import App_Manage_Window

alignleft = sg.TEXT_LOCATION_LEFT
aligncenter = sg.TEXT_LOCATION_CENTER
alignright = sg.TEXT_LOCATION_RIGHT

def workspace_window():

    # ----------------------------------define variables-------------------------------
    #graph global variables
    color1 = None
    color2 = None
    color3 = None
    color4 = None
    color5 = None
    color6 = None
    color7 = None
    color8 = None

    #temporary lists
    list_script_temp = []
    list_text_temp = []
    list_of_script = []
    list_of_text = []

    #lists with values to be used in Listboxes
    ListOfColors = ["Red", "Yellow", "Cyan", "Magenta", "Green1", "Black", "White"]
    ListOfFont = ["Default", "Defaut and Bold", "Bigger and Bold"]
    ListOfJustification = ["Left Orientation", "Center Orientation", "Right Orientation"]
    ListOfFlash = ["Ultra Fast", "Super Fast", "Very Fast", "Fast", "Medium", "Slow", "Very Slow", "Super Slow", "Ultra Slow", "No Flash"]
    ListOfWidth = ["Thinnest", "Ultra thin", "Super thin", "Very thin", "Thin", "Medium", "Thick", "Very thick", "Super thick", "Ultra thick", "You really don't need that!", "Thickest"]
    ListOfSize = ["Default size and bold", "Bigger size and bold", "Default size"]
    ListOfIntegerClearLast = App_Functions.get_string_integer(list(range(0, 100)))
    ListOfFloatMav = App_Functions.get_string_integer([i / 10.0 for i in range(10000)])
    ListOfAmmo = App_Functions.get_string_integer(list(range(0, 10000)))
    ListOfSwitch = ["OFF", "ON"]
    ListOfFuelFoward = App_Functions.get_string_integer(list(range(0, 2780, 10)))
    ListOfFuelAft = App_Functions.get_string_integer(list(range(0, 2340, 10)))
    ListOfFuelReservoir = App_Functions.get_string_integer(list(range(0, 490, 10)))
    ListOfFuelWing = App_Functions.get_string_integer(list(range(0, 560, 11)))
    ListOfFuelExtWing = App_Functions.get_string_integer(list(range(0, 2520, 4)))
    ListOfFuelExtCtr = App_Functions.get_string_integer(list(range(0, 2050, 40)))
    ListOfTimeSeconds = App_Functions.get_string_integer(list(range(1, 3601)))
    ListOfCoordinate = App_Functions.make_coordinates()
    ListOfDegreesX = [f"{abs(i)} right" if i < 0
                     # Positive numbers are "left"
                     else f"{i} left"
                     for i in range(-360, 361, 5)] # Exclude 0, as it's neither positive nor negative
    ListOfDegreesY = [f"{abs(i)} up" if i < 0
                     # Positive numbers are "left"
                     else f"{i} down"
                     for i in range(-360, 361, 5)] # Exclude 0, as it's neither positive nor negative
           
    #list to be used in sg Objects
    headings = ["Function", "1st Argument", "2nd Argument", "3rd Argument", "4th Argument", "5th Argument"]
    create_tooltips = ["a", "b"]

    # ----------------------------------create Tree Data--------------------------------
    # Create a TreeData object
    tree_data = sg.TreeData()

    # Get Sample data from App_Tree
    options_data = App_Tree.functions_in_tree()

    # Populate the TreeData object from the options data
    for item in options_data:
        key, parent_key, text, values_list, icon = item
        tree_data.Insert(parent_key, key, text, values_list, icon)

    # ----------------------------------create Menu Data--------------------------------
    menu_def = [['File', ['Open', 'Delete', 'Save', 'Save as', 'Close']],
                ['Samples', ['Header', 'Text', 'highlight text']], 
                ['Help', ["Basic Concepts", "Functions", "Arguments", "Coordinates"]], 
                ['About...', "Version"],]
    
    # ----------------------------------create Layout--------------------------------
    # Create buttons column
    buttons_col = sg.Frame("Options: ", [[sg.Button(button_text = "Set\n Parameters", disabled = True, size = (14, 3), font = "_ 10", enable_events = True, key = "-BPAR-")],
                                         [sg.Button(button_text = "Add\n Function", disabled = True, size = (14, 3), font = "_ 10", enable_events = True, key = "-BADD-")],
                                         [sg.Button(button_text = "Edit", disabled = True, size = (14, 3), font = "_ 10", enable_events = True, key = "-BEDT-")],
                                         [sg.Button(button_text = "Delete", disabled = True, size = (14, 3), font = "_ 10", enable_events = True, key = "-BDEL-")],
                                         [sg.Button(button_text = "Function\n Help", disabled = True, size = (14, 3), font = "_ 10", enable_events = True, key = "-BHEL-")]],
                           title_color = "#ffffff", font = "_ 14", background_color = "#64778d", size=(90,720), vertical_alignment = "top")  
    
    # Create functions column with Tree element
    function_col = sg.Frame("Functions: ", [[sg.Tree(data=tree_data,
                                             auto_size_columns=False,
                                             num_rows=40,
                                             col0_width=50,  # Width of the first column (the tree structure)
                                             key='-tree-',
                                             row_height = 20,
                                             show_expanded=False,  # Start with some nodes expanded
                                             enable_events=True,  # VERY IMPORTANT: This enables events for the tree
                                             expand_y=True)]], 
                            title_color = "#ffffff", font = "_ 14", background_color = "#64778d", size=(455,720), vertical_alignment = "top")  

    
    # Create graphic column with Graph element and information fields
    graph_col = sg.Frame("Graphic:", [[sg.Graph((912, 519), (-1,-1), (1, 1), background_color = "black", key = "-graph-")],  
                                      [sg.Checkbox("Show grid.", background_color = "#64778d", checkbox_color = "#ffffff", default = False, enable_events = True,  key = "-grid-"), 
                                       sg.Checkbox("Show shapes.", background_color = "#64778d", checkbox_color = "#ffffff", default = False, enable_events = True,  key = "-shape-"), 
                                       sg.Checkbox("Show cockpit.", background_color = "#64778d", checkbox_color = "#ffffff", default = True, enable_events = True,  key = "-ckpt-"),
                                       sg.Text("Last cursor position in script:  ", background_color = "#64778d", text_color = ("yellow")), 
                                       sg.Text("0.00", background_color = "#64778d", text_color = ("yellow"), key = "-cposx-"), 
                                       sg.Text("0.00", background_color = "#64778d", text_color = ("yellow"), key = "-cposy-"),
                                       sg.Text(" ", background_color = "#64778d", text_color = ("red"), key = "-limtxt-")],
                                      [sg.HorizontalSeparator(color = "#64778d")],
                                      [sg.Text("Script Function Syntax: ", background_color = "#64778d",), 
                                       sg.Text(" ", background_color = "#64778d", text_color = ("#ffffff"), key = "-scpt-")],
                                      [sg.Text("What this function does: ", background_color = "#64778d",), 
                                       sg.Text(" ", background_color = "#64778d", text_color = ("yellow"), key = "-desc-")],
                                      [sg.Text("What You must provide: ", background_color = "#64778d"), 
                                       sg.Text(" ", background_color = "#64778d", text_color = ("gold2"), key = "-synt-")],
                                      [sg.Text("Tips how to use it: ", background_color = "#64778d"),
                                       sg.Text(" ", background_color = "#64778d", text_color = ("bisque"), key = "-exem-")],],
                         title_color = "#ffffff", font = "_ 14", background_color = "#64778d", size = (932, 720), vertical_alignment = "top") 

    # Create summary column with Multiline element
    summary_col = sg.Frame("Summary:", [[sg.Multiline(auto_refresh = True,
                                                            font = ("_, 10"),
                                                            background_color = "light gray",
                                                            size = (400,720),
                                                            justification = "left",
                                                            wrap_lines = True,
                                                            key = "-FILE_TEXT-",)]], 
                         title_color = "#ffffff",  font = "_ 14", background_color = "#64778d", size = (400, 720), vertical_alignment = "top")

    # Create script column with Table element
    script_col = sg.Frame("Script:", [[sg.Table(list_of_script,
                                                font = ("_, 10"),
                                                headings = headings,
                                                header_font = ("_, 10"),
                                                header_background_color = "#91a6be",
                                                def_col_width = 26,
                                                background_color = "#d4d7dd",
                                                alternating_row_color = "#ffffff",
                                                auto_size_columns = False,
                                                display_row_numbers = True,
                                                starting_row_number = 1,
                                                selected_row_colors = ("#ffffff", "#64778d"),
                                                size = (1490, 250),
                                                justification = "left", 
                                                key = "-SCRIPT-")]], 
                          title_color = "#ffffff",  font = "_ 14", background_color = "#64778d", size = (1492, 260), vertical_alignment = "top") 

    # Create shortcuts column with Buttons
    shorcut_col = sg.Frame("Shortcuts:", [[sg.Button(button_text = "Cursor at 0.0", size = (14), enable_events = True, disabled = True, key = "-SHORT1-"), 
                                       sg.Button(button_text = "Cursor -0.98/0.08", size = (14), enable_events = True, disabled = True, key = "-SHORT2-"),
                                       sg.Button(button_text = "Move Cursor -0.04", size = (14), enable_events = True, disabled = True, key = "-SHORT3-")],
                                      [sg.Button(button_text = "Short4", size = (14), enable_events = True, disabled = True, key = "-SHORT4-"),
                                       sg.Button(button_text = "Short5", size = (14), enable_events = True, disabled = True, key = "-SHORT5-"),
                                       sg.Button(button_text = "Short6", size = (14), enable_events = True, disabled = True, key = "-SHORT6-")], 
                                      [sg.Button(button_text = "Short7", size = (14), enable_events = True, disabled = True, key = "-SHORT7-"),
                                       sg.Button(button_text = "Short8", size = (14), enable_events = True, disabled = True, key = "-SHORT8-"),
                                       sg.Button(button_text = "Short9", size = (14), enable_events = True, disabled = True, key = "-SHORT9-")],
                                      [sg.Button(button_text = "Short10", size = (14), enable_events = True, disabled = True, key = "-SHORT10-"),
                                       sg.Button(button_text = "Short6", size = (14), enable_events = True, disabled = True, key = "-SHORT11-"), 
                                       sg.Button(button_text = "Short7", size = (14), enable_events = True, disabled = True, key = "-SHORT12-")],
                                      [sg.Button(button_text = "Short10", size = (14), enable_events = True, disabled = True, key = "-SHORT14-"),
                                       sg.Button(button_text = "Short6", size = (14), enable_events = True, disabled = True, key = "-SHORT14-"), 
                                       sg.Button(button_text = "Short7", size = (14), enable_events = True, disabled = True, key = "-SHORT15-")],
                                      [sg.Button(button_text = "Short8", size = (14), enable_events = True, disabled = True, key = "-SHORT16-"),
                                       sg.Button(button_text = "Short9", size = (14), enable_events = True, disabled = True, key = "-SHORT17-"),
                                       sg.Button(button_text = "Short10", size = (14), enable_events = True, disabled = True, key = "-SHORT18-")],
                                      [sg.Button(button_text = "Short8", size = (14), enable_events = True, disabled = True, key = "-SHORT19-"),
                                       sg.Button(button_text = "Short9", size = (14), enable_events = True, disabled = True, key = "-SHORT20-"),
                                       sg.Button(button_text = "Short10", size = (14), enable_events = True, disabled = True, key = "-SHORT21-")]],
                           title_color = "#ffffff",  font = "_ 14", background_color = "#64778d", size = (400, 260), vertical_alignment = "top")

    # ----------------------------------create Window--------------------------------
    layout = [[sg.Menu(menu_def)],[buttons_col, function_col, graph_col, summary_col],[script_col, shorcut_col]] 

    workspace_window = sg.Window("Create Script", 
                            layout, 
                            icon = App_Images.start_icon, 
                            return_keyboard_events = False, 
                            finalize = True, 
                            resizable = True,
                            modal = False,
                            location = (50, 50), 
                            size = (1820, 900))

    ckpt_image1 = workspace_window["-graph-"].draw_image(data = App_Images.cockpit_image1, location = (-1, 1))
    graph = workspace_window["-graph-"].draw_text(">>> Graphics not in game scale! <<<", (-0.00, 0.95), color = "Red", font = "arial 10 bold")

    selected = ""

    # ----------------------------------Manage Events--------------------------------
    while True:
        
        event, values = workspace_window.read()
        print(">>WIN/CREATE - events: ", event)

       #close application event
        if event in (sg.WIN_CLOSED, "Close"):
            print(">>win/create - event: exit/close")
            break

        #Handle tree selection (functions) events 
        if event == "-tree-":
            print("tree test")
            selected = values['-tree-'][0]
            App_Tree.handle_tree_selection(workspace_window, selected)
        elif event == "-BADD-" and selected == "-layclr-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "Clear\n", "Clear all elements off screen at once.", None, None, None)
        elif event == "-BADD-" and selected == "-secwhl-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "While\n", "Run the commands in section while a value is TRUE.", None, None, None)
        elif event == "-BADD-" and selected == "-secwhln-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "WhileNot\n", "Run the commands in section while a value is FALSE.", None, None, None)
        elif event == "-BADD-" and selected == "-secend-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "EndSection\n", "End of section.", None, None, None)
        elif event == "-BADD-" and selected == "-othends-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "EndScript\n", "End of script", None, None, None)
        elif event == "-BADD-" and selected == "-othent-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "EnterCritical\n", "Execute multiple commands all at once.", None, None, None)
        elif event == "-BADD-" and selected == "-othend-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "EndCritical\n", "Multiple commands execution terminated.", None, None, None)
        elif event == "-BADD-" and selected == "-bolif-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "If\n", "Check if the value of last command is TRUE.", None, None, None)
        elif event == "-BADD-" and selected == "-bolifn-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "IfNot\n", "Check if the value of last command is FALSE.", None, None, None)
        elif event == "-BADD-" and selected == "-timwow-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "WaitForNoWOW\n", "Script paused until aircraf is airborne.", None, None, None)
        elif event == "-BADD-" and selected == "-othline-":
            App_Functions.Handle_Function(workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "\n", " ", None, None, None)
        elif event == "-BPAR-" and selected == "-othcom-":
            App_Popups_Window.input_popup("Add a comment line to your script", workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, "//", ">> Script commented:  ")
        elif event == "-BPAR-" and selected == "-secname-":
            App_Popups_Window.section_popup("Define the name of your section", workspace_window, list_script_temp, list_text_temp, list_of_script, list_of_text, ">> A section has been defined:  ")
        elif event == "-BPAR-" and selected == "-imsfuel-":
            App_Popups_Window.fuel_window(workspace_window, ListOfFuelFoward, ListOfFuelAft,  ListOfFuelReservoir, ListOfFuelWing, ListOfFuelExtWing, ListOfFuelExtCtr, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetFuel", ">> Total amount of fuel set to:  ")
        elif event == "-BPAR-" and selected == "-layall-":
            App_Popups_Window.list_popup("Choose a color for all objects", workspace_window, ListOfColors, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetColor", ">> The color for all objects has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-laytxt-":
            App_Popups_Window.list_popup("Choose a color for texts", workspace_window, ListOfColors, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetFontColor", ">> The color for texts has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-layshp-":
            App_Popups_Window.list_popup("Choose a color for draws", workspace_window, ListOfColors, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetDrawColor", ">> The color for draws has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-laybcg-":
            App_Popups_Window.list_popup("Choose a color for text background", workspace_window, ListOfColors, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetFontBGColor", ">> The color for text background has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-layfsh-":
            App_Popups_Window.list_popup("Choose a flash rate for all objects", workspace_window, ListOfFlash, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetFlash", ">> Flash rate for all objects has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-layfsht-":
            App_Popups_Window.list_popup("Choose a flash rate texts", workspace_window, ListOfFlash, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetFontFlash", ">> Flash rate for texts has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-layfshd-":
            App_Popups_Window.list_popup("Choose a flash rate for draws", workspace_window, ListOfFlash, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetDrawFlash", ">> Flash rate for draws has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-layfon-":
            App_Popups_Window.list_popup("Choose font size", workspace_window, ListOfSize, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetFont", ">> Font size has been defined:  ", 20)
        elif event == "-BPAR-" and selected == "-layjus-":
            App_Popups_Window.list_popup("Choose a text justification", workspace_window, ListOfJustification, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetTextOrientation", ">> Text justification has been set:  ", 20)
        elif event == "-BPAR-" and selected == "-layline-":
            App_Popups_Window.list_popup("Define the line width", workspace_window, ListOfWidth, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetLineWidth", ">> All lines width has been defined:  ", 20)
        elif event == "-BPAR-" and selected == "-layclrl-":
            App_Popups_Window.list_popup("Set the amount of last elements do be removed", workspace_window, ListOfIntegerClearLast, list_script_temp, list_text_temp, list_of_script, list_of_text, "ClearLast", ">> This last amount of elements will be removed from screen:  ", 10)
        elif event == "-BPAR-" and selected == "-laybcgs-":
            App_Popups_Window.list_popup("Turn background text ON or OFF", workspace_window, ListOfSwitch, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetTextBoxed", ">> Text boxing has been turned:  ", 10)
        elif event == "-BPAR-" and selected == "-imsgun-":
            App_Popups_Window.list_popup("Define an ammount of ammo for you cannon (don't be greedy!)", workspace_window, ListOfAmmo, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetGunAmmo", ">> Amount of cannon rounds set to:  ", 10)
        elif event == "-BPAR-" and selected == "-ims65-":
            App_Popups_Window.list_popup("Define the spool up time for your AGM-65 (Default is 180.0)", workspace_window, ListOfFloatMav, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetMavCoolTime", ">> Amount of Mav spoon up seconds set to:  ",  10)
        elif event == "-BPAR-" and selected == "-timwtr-":
            App_Popups_Window.list_popup("Set how many seconds the script will be paused in REAL time", workspace_window, ListOfTimeSeconds, list_script_temp, list_text_temp, list_of_script, list_of_text, "Wait", ">> Pause script for (REAL time seconds):  ",  10)
        elif event == "-BPAR-" and selected == "-timwtg-":
            App_Popups_Window.list_popup("Set how many seconds the script will be paused in GAME time", workspace_window, ListOfTimeSeconds, list_script_temp, list_text_temp, list_of_script, list_of_text, "WaitGameTime", ">> Pause script for (GAME time seconds):  ",  10)
        elif event == "-BPAR-" and selected == "-soustop-":
            App_Popups_Window.list_popup("Set how many seconds the script will be paused", workspace_window, ListOfTimeSeconds, list_script_temp, list_text_temp, list_of_script, list_of_text, "WaitSoundStop", ">> Pause script for end of sound or seconds:  ",  10)
        elif event == "-BPAR-" and selected == "-outtxt-":
            App_Popups_Window.list_input_popup("Set the time and text to be shown on the screen", workspace_window, ListOfTimeSeconds, list_script_temp, list_text_temp, list_of_script, list_of_text, "Print", ">>T ext shows for a period (script not holded):  ", 10)
        elif event == "-BPAR-" and selected == "-outtxtw-":
            App_Popups_Window.list_input_popup("Set the time and text to be shown on the screen", workspace_window, ListOfTimeSeconds, list_script_temp, list_text_temp, list_of_script, list_of_text, "WaitPrint", ">> Text shows for a period (script holded):  ", 10)
        elif event == "-BPAR-" and selected == "-cposet-":
            App_Popups_Window.list_list_popup("Define a cursor position (x, y)", workspace_window, ListOfCoordinate, ListOfCoordinate, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetCursor", ">> Set cursor to position (x, y):  ", 10, 10)
        elif event == "-BPAR-" and selected == "-cpomov-":
            App_Popups_Window.list_list_popup("Move the position of the cursor by", workspace_window, ListOfCoordinate, ListOfCoordinate, list_script_temp, list_text_temp, list_of_script, list_of_text, "MoveCursor", ">> Cursor position moved by:  ", 10, 10)
        elif event == "-BPAR-" and selected == "-coppan-":
            App_Popups_Window.list_list_popup("Set the pilot's POV position to", workspace_window, ListOfDegreesX, ListOfDegreesY, list_script_temp, list_text_temp, list_of_script, list_of_text, "SetPanTilt", ">> Pilot's POV set to (degrees):  ", 10, 10)
        elif event == "-BPAR-" and selected == "-copmove-":
            App_Popups_Window.list_list_popup("Move the pilot's POV to", workspace_window, ListOfDegreesX, ListOfDegreesY, list_script_temp, list_text_temp, list_of_script, list_of_text, "MovePanTilt", ">> Pilot's POV moved about (degrees):  ", 10, 10)




        if event == "-BHEL-" and values["-tree-"][0] == "-othcom-":
            print(">> BMS Manual text - Comment:", event)
            App_Manual.manual_comment("-COMMENT-")

        #Handling MENU Events

        if event == "Delete":
            print("event menu: delete")
            App_Manage_Window.manage_window()
        if event == 'Version':
            print("event menu: about")
            sg.popup("""Falcon BMS Training Script Designer. 
Version 1.4 sep/25.
FreeSimpleGUI Copyright 2024, 2022 PySimpleGui.
by Sassah Wingman.""", title = None, no_titlebar = True, keep_on_top = True, modal = True)
        elif event == "Functions" and values["-COMMENT-"] == True:
            print(">> BMS Manual text - Comment:", event)
            App_Manual.manual_comment("-COMMENT-")
        elif event == "Functions" and values["-LINE-"] == True:
            print(">> BMS Manual text - Space line:", event)
            App_Manual.manual_comment("-LINE-")
        elif event == "Functions" and values["-CURSORP-"] == True:
            print(">> BMS Manual text - Cursor Position:", event)
            App_Manual.manual_comment("-CURSORP-")
        elif event == "Functions" and values["-CURSORM-"] == True:
            print(">> BMS Manual text - Move Cursor:", event)
            App_Manual.manual_comment("-CURSORM-")
        elif event == "Functions" and values["-COLOR-"] == True:
            print(">> BMS Manual text - Color:", event)
            App_Manual.manual_comment("-COLOR-")
        elif event == "Functions" and values["-COLORT-"] == True:
            print(">> BMS Manual text - Text Color:", event)
            App_Manual.manual_comment("-COLORT-")
        elif event == "Functions" and values["-COLORD-"] == True:
            print(">> BMS Manual text - Draw Color:", event)
            App_Manual.manual_comment("-COLORD-")
        elif event == "Functions" and values["-FLASH-"] == True:
            print(">> BMS Manual text - Flash:", event)
            App_Manual.manual_comment("-FLASH-")
        elif event == "Functions" and values["-FLASHT-"] == True:
            print(">> BMS Manual text - Font Flash:", event)
            App_Manual.manual_comment("-FLASHT-")
        elif event == "Functions" and values["-FLASHD-"] == True:
            print(">> BMS Manual text - Draw Flash:", event)
            App_Manual.manual_comment("-FLASHD-") 
        elif event == "Functions" and values["-FONT-"] == True:
            print(">> BMS Manual text - Font Size:", event)
            App_Manual.manual_comment("-FONT-")
        elif event == "Functions" and values["-JUST-"] == True:
            print(">> BMS Manual text - Justification:", event)
            App_Manual.manual_comment("-JUST-")   
        elif event == "Functions" and values["-LINEW-"] == True:
            print(">> BMS Manual text - Line Width:", event)
            App_Manual.manual_comment("-LINEW-")
        elif event == "Functions" and values["-LINE-"] == True:
            print(">> BMS Manual text - Draw Line:", event)
            App_Manual.manual_comment("-LINE-")
        elif event == "Functions" and values["-OVAL-"] == True:
            print(">> BMS Manual text - Draw Oval:", event)
            App_Manual.manual_comment("-OVAL-")
        elif event == "Functions" and values["-PRINT-"] == True:
            print(">> BMS Manual text - Print:", event)
            App_Manual.manual_comment("-PRINT-")
        elif event == "Functions" and values["-PRINTW-"] == True:
            print(">> BMS Manual text - Wait Print:", event)
            App_Manual.manual_comment("-PRINTW-")  
        elif event == "Functions" and values["-CLEAR-"] == True:
            print(">> BMS Manual text - Clear:", event)
            App_Manual.manual_comment("-CLEAR-")  
        elif event == "Functions" and values["-CLEARL-"] == True:
            print(">> BMS Manual text - Clear Last:", event)
            App_Manual.manual_comment("-CLEARL-") 
        
        elif event == "Coordinates":
             print(">> BMS Manual text - coordinates: ", event)
             App_Manual.manual_comment("-coord-")
        elif event == "Arguments":
             print(">> BMS Manual text - coordinates: ", event)
             App_Manual.manual_comment("-argm-")
        elif event == "Functions":
            sg.popup_auto_close("Select a function before using the Help/Functions menu.", auto_close_duration = 3)
  
       
        
        if event == "-grid-":
            print(">>win/create - values in GRID: ", values["-grid-"])
            if values["-grid-"] == True:
                #draw vertical and horizontal lines
                line1 = workspace_window["-graph-"].draw_line((0.50, 1), (0.50, -1), color = "yellow", width = 1)
                line2 = workspace_window["-graph-"].draw_line((-0.50, 1), (-0.50, -1), color = "yellow", width = 1)
                line3 = workspace_window["-graph-"].draw_line((1, 0.50), (-1, 0.50), color = "yellow", width = 1)
                line4 = workspace_window["-graph-"].draw_line((1, -0.50), (-1, -0.50), color = "yellow", width = 1)
                line5 = workspace_window["-graph-"].draw_line((0,1), (0, -1), color = "yellow", width = 3)
                line6 = workspace_window["-graph-"].draw_line((1,0), (-1, 0), color = "yellow", width = 3)
                line7 = workspace_window["-graph-"].draw_line((-0.52, -0.70), (-0.52, -0.30), color = "red", width = 1)
                line8 = workspace_window["-graph-"].draw_line((-0.70, -0.52), (-0.30, -0.52), color = "red", width = 1)
                print(">>win/create - lines id: ", line1, line2, line3, line4, line5, line6, line7, line8)
                
                #Display coordinates
                coord1 = workspace_window["-graph-"].draw_text("0.0   0.0", (0, 0.06), color = "yellow", font = "arial 12 bold")
                coord2 = workspace_window["-graph-"].draw_text("-1.0 / 1.0", (-0.88, 0.95), color = "yellow", font = "arial 12 bold")
                coord3 = workspace_window["-graph-"].draw_text("-1.0 / -1.0", (-0.88, -0.95), color = "yellow", font = "arial 12 bold")
                coord4 = workspace_window["-graph-"].draw_text(" 1.0 / 1.0", (0.88, 0.95), color = "yellow", font = "arial 12 bold")
                coord5 = workspace_window["-graph-"].draw_text(" 1.0 / -1.0", (0.88, -0.95), color = "yellow", font = "arial 12 bold")
                coord6 = workspace_window["-graph-"].draw_text("0.02 interval", (-0.68, -0.45), color = "red", font = "arial 12 bold")
                print(">>win/create - coord id: ", coord1, coord2, coord3, coord4, coord5, coord6)
            else:
                #delete lines
                workspace_window["-graph-"].delete_figure(line1)
                workspace_window["-graph-"].delete_figure(line2)
                workspace_window["-graph-"].delete_figure(line3)
                workspace_window["-graph-"].delete_figure(line4)
                workspace_window["-graph-"].delete_figure(line5)
                workspace_window["-graph-"].delete_figure(line6)
                workspace_window["-graph-"].delete_figure(line7)
                workspace_window["-graph-"].delete_figure(line8)
                #delete coordinates
                workspace_window["-graph-"].delete_figure(coord1)
                workspace_window["-graph-"].delete_figure(coord2)
                workspace_window["-graph-"].delete_figure(coord3)
                workspace_window["-graph-"].delete_figure(coord4)
                workspace_window["-graph-"].delete_figure(coord5)
                workspace_window["-graph-"].delete_figure(coord6)
                
        if event == "-ckpt-":
            if values["-ckpt-"] == True:
                print(">>win/create - values in ckpt: ", values["-ckpt-"])
                #workspace_window["-graph-"].erase()
                workspace_window["-graph-"].delete_figure(ckpt_image1)
                workspace_window["-grid-"].update(False)
                ckpt_image1 = workspace_window["-graph-"].draw_image(data = App_Images.cockpit_image1, location = (-1, 1))
                graph = workspace_window["-graph-"].draw_text(">>> Graphics not in game scale! <<<", (-0.00, 0.95), color = "Red", font = "arial 10 bold")
                print(">>win/create - cockpit image id:", ckpt_image1)
            else:
                workspace_window["-graph-"].delete_figure(ckpt_image1)

        if event == "-shape-":
            print(">>win/create - values in SHAPED: ", values["-shape-"])
            if values["-shape-"] == True:
                #draw lines, circles
                shape1 = workspace_window["-graph-"].draw_circle((0.55, 0.45), radius = 0.1, line_color = "cyan", line_width = 2)
                shape2 = workspace_window["-graph-"].draw_circle((0.55, 0.45), radius = 0.05, line_color = "yellow", line_width = 1)
                shape3 = workspace_window["-graph-"].draw_oval((-0.60, 0.60), (-0.25, 0.25), line_color = "green1", line_width = 2)
                shape5 = workspace_window["-graph-"].draw_line((-0.40, -0.60), (-0.08, -0.35), color = "red", width = 2)
                shape4 = workspace_window["-graph-"].draw_rectangle((-0.81, -0.06), (-0.49, -0.10), line_color = "yellow", fill_color = "yellow", line_width = 2)
                shape6 = workspace_window["-graph-"].draw_text("this is a text!", (-0.80, -0.00), font = "arial 8",  color = "white", text_location = alignleft)
                shape7 = workspace_window["-graph-"].draw_text("this is a boxed text!", (-0.80, -0.08), font = "arial 8",  color = "black", text_location = alignleft)
                
                print(">>win/create - lines id: ", shape1, shape2, shape3, shape4, shape5, shape6, shape7)
            else:
                workspace_window["-graph-"].delete_figure(shape1)
                workspace_window["-graph-"].delete_figure(shape2)
                workspace_window["-graph-"].delete_figure(shape3)
                workspace_window["-graph-"].delete_figure(shape4)
                workspace_window["-graph-"].delete_figure(shape5)
                workspace_window["-graph-"].delete_figure(shape6)
                workspace_window["-graph-"].delete_figure(shape7)



    workspace_window.close()  
    return workspace_window



