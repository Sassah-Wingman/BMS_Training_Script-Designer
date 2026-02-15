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

       
        
        
        #Draw a line
        elif event == "-LINE-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            App_Functions.clear_fields(workspace_window)
            workspace_window["-scpt-"].update("Line <time> <float (x1)> <float (y1)> <float (x2)> <float (y2)>")
            workspace_window["-desc-"].update("Draws a line for <time> duration from x1, y1 to x2, y2 coordinates.")
            workspace_window["-synt-"].update("Enter a time followed by x and y coordinates. Range from -1.00 to 1.00.")
            workspace_window["-exem-"].update("This function is not dependent from the current cursor location.")
            workspace_window["-ADDLINE-"].update(visible = True)
            workspace_window["-ARGLINETM-"].update(disabled = False, value = " ")
            workspace_window["-ARGLINETM-"].set_focus(force = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("Line")
            list_text_temp.append("Draw a line: ")
            print(">>win/create - cursorp - list functemp script: ", list_script_temp)
            print(">>win/create - cursorp - list functemp text: ", list_text_temp)
        #Draw an oval/circle
        elif event == "-OVAL-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            App_Functions.clear_fields(workspace_window)
            workspace_window["-scpt-"].update("Oval <time> <float (radius x)> <float (radius y) optional>")
            workspace_window["-desc-"].update("Draws an oval or circle for <time> duration at the current position of the cursor.")
            workspace_window["-synt-"].update("Enter a time followed by radius value. Range from -1.00 to 1.00.")
            workspace_window["-exem-"].update("Set the cursor position first. If only one argument is supplied, then a circle is drawn.")
            workspace_window["-ADDOVAL-"].update(visible = True)
            workspace_window["-ARGOVALTM-"].update(disabled = False, value = " ")
            workspace_window["-ARGOVALTM-"].set_focus(force = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("Oval")
            list_text_temp.append("Draw an oval/circle: ")
            print(">>win/create - cursorp - list functemp script: ", list_script_temp)
            print(">>win/create - cursorp - list functemp text: ", list_text_temp)




        elif event == "-SHORT1-":
            is_a_floatx = float("0.0")
            is_a_floaty = float("0.0")
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            color2 = workspace_window["-graph-"].draw_rectangle((is_a_floatx - 0.01, is_a_floaty + 0.02), (is_a_floatx + 0.01, is_a_floaty - 0.02), fill_color = "yellow", line_color = "magenta")  
            color1 = workspace_window["-graph-"].draw_text("+", (is_a_floatx, is_a_floaty), color = "blue", font = "arial 12")
            workspace_window["-cposx-"].update(is_a_floatx)
            workspace_window["-cposy-"].update(is_a_floaty)
            workspace_window["-ARGCURSORPX-"].update(is_a_floatx)
            workspace_window["-ARGCURSORPY-"].update(is_a_floaty)
            workspace_window["-ADDCURSORP-"].update(disabled = False)
            posx = App_Functions.global_coordinatex(values["-ARGCURSORPX-"], values["-ARGCURSORMX-"])
            posy = App_Functions.global_coordinatey(values["-ARGCURSORPY-"], values["-ARGCURSORMY-"])
            print("float test shortcut1 posx & posy: ", is_a_floatx, is_a_floaty)
        elif event == "-SHORT2-":
            is_a_floatx = float("-0.98")
            is_a_floaty = float("0.08")
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            color2 = workspace_window["-graph-"].draw_rectangle((is_a_floatx - 0.01, is_a_floaty + 0.02), (is_a_floatx + 0.01, is_a_floaty - 0.02), fill_color = "yellow", line_color = "magenta")  
            color1 = workspace_window["-graph-"].draw_text("+", (is_a_floatx, is_a_floaty), color = "blue", font = "arial 12")
            workspace_window["-cposx-"].update(is_a_floatx)
            workspace_window["-cposy-"].update(is_a_floaty)
            workspace_window["-ARGCURSORPX-"].update(is_a_floatx)
            workspace_window["-ARGCURSORPY-"].update(is_a_floaty)
            workspace_window["-ADDCURSORP-"].update(disabled = False)
            posx = App_Functions.global_coordinatex(values["-ARGCURSORPX-"], values["-ARGCURSORMX-"])
            posy = App_Functions.global_coordinatey(values["-ARGCURSORPY-"], values["-ARGCURSORMY-"])
            print("float test shortcut2 posx & posy: ", is_a_floatx, is_a_floaty)
            
       
                
                #edit color
        elif event == "-ARGCOLOR-" and values["-ARGCOLOR-"] in ListOfColors:
            print(">>win/create - combo COLORT: ", values["-ARGCOLORT-"])
            workspace_window["-ADDCOLOR-"].update(disabled = False)
            color1 = workspace_window["-graph-"].draw_text("This is the color you picked!", (-0.75, -0.08), color = values["-ARGCOLOR-"], font = "arial 8 bold")
            color2 = workspace_window["-graph-"].draw_line((-0.80, -0.80), (-0.60, -0.60), color = values["-ARGCOLOR-"], width = 1)
            color3 = workspace_window["-graph-"].draw_line((-0.80, -0.70), (-0.60, -0.50), color = values["-ARGCOLOR-"], width = 2)
            color4 = workspace_window["-graph-"].draw_line((-0.80, -0.60), (-0.60, -0.40), color = values["-ARGCOLOR-"], width = 3)
            color5 = workspace_window["-graph-"].draw_line((-0.80, -0.50), (-0.60, -0.30), color = values["-ARGCOLOR-"], width = 4)
            color6 = workspace_window["-graph-"].draw_circle((0.40, 0.60), radius = 0.15, line_color = values["-ARGCOLOR-"], line_width = 2)
            color7 = workspace_window["-graph-"].draw_circle((0.40, 0.60), radius = 0.10, line_color = values["-ARGCOLOR-"], line_width = 1)
            color8 = workspace_window["-graph-"].draw_oval((0.50, -0.50), (0.25, -0.25), line_color = values["-ARGCOLOR-"], line_width = 2)
        #edit text color
        elif event == "-ARGCOLORT-" and values["-ARGCOLORT-"] in ListOfColors:
            print(">>win/create - combo COLORT: ", values["-ARGCOLORT-"])
            workspace_window["-ADDCOLORT-"].update(disabled = False)
            color1 = workspace_window["-graph-"].draw_text("This is the color of your text!", (-0.95, -0.08), color = values["-ARGCOLORT-"],text_location = alignleft, font = "arial 8 bold")
        #edit draw color
        elif event == "-ARGCOLORD-" and values["-ARGCOLORD-"] in ListOfColors:
            print(">>win/create - combo COLORT: ", values["-ARGCOLORD-"])
            workspace_window["-ADDCOLORD-"].update(disabled = False)
            color2 = workspace_window["-graph-"].draw_line((-0.80, -0.80), (-0.60, -0.60), color = values["-ARGCOLORD-"], width = 1)
            color3 = workspace_window["-graph-"].draw_line((-0.80, -0.70), (-0.60, -0.50), color = values["-ARGCOLORD-"], width = 2)
            color4 = workspace_window["-graph-"].draw_line((-0.80, -0.60), (-0.60, -0.40), color = values["-ARGCOLORD-"], width = 3)
            color5 = workspace_window["-graph-"].draw_line((-0.80, -0.50), (-0.60, -0.30), color = values["-ARGCOLORD-"], width = 4)
            color6 = workspace_window["-graph-"].draw_circle((0.40, 0.60), radius = 0.15, line_color = values["-ARGCOLORD-"], line_width = 2)
            color7 = workspace_window["-graph-"].draw_circle((0.40, 0.60), radius = 0.10, line_color = values["-ARGCOLORD-"], line_width = 1)
            color8 = workspace_window["-graph-"].draw_oval((0.50, -0.50), (0.25, -0.25), line_color = values["-ARGCOLORD-"], line_width = 2)
        #edit text justification
        elif event == "-ARGJUST-":
            print(">>win/create - combo justification: ", values["-ARGJUST-"])
            workspace_window["-ADDJUST-"].update(disabled = False)
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            if values["-ARGJUST-"] == ListOfJustification[0]:
                print(">>win/create - combo justification index 0: ", ListOfFont[0])
                color1 = workspace_window["-graph-"].draw_text("Left justified text!", (-0.95, -0.08), color = "yellow", text_location = alignleft, font = "arial 8 bold")
            elif values["-ARGJUST-"]== ListOfJustification[1]:
                print(">>win/create - combo justification index 1: ", ListOfFont[1])
                color1 = workspace_window["-graph-"].draw_text("Center justified text!", (-0.65, -0.08), color = "yellow", text_location = aligncenter, font = "arial 8 bold")
            elif values["-ARGJUST-"] == ListOfJustification[2]:
                print(">>win/create - combo justification index 2: ", ListOfFont[2])
                color1 = workspace_window["-graph-"].draw_text("Right justified text!", (-0.35, -0.08), color = "yellow", text_location = alignright, font = "arial 8 bold")
        #edit boxed text color
        elif event == "-ARGCOLORB-" and values["-ARGCOLORB-"] in ListOfColors:   
            print(">>win/create - combo COLORB: ", values["-ARGCOLORB-"])
            workspace_window["-ARGCOLORT-"].update(disabled = False, background_color = "#ffffff")
            workspace_window["-COLORT-"].update(text = "Test a text over background >>>", disabled = True)
            workspace_window["-ADDCOLORB-"].update(disabled = False)
            color2 = workspace_window["-graph-"].draw_rectangle((-0.98, -0.05), (-0.40, -0.11), fill_color = values["-ARGCOLORB-"], line_color = values["-ARGCOLORB-"]) 
        # turn boxed text color on and off
        elif event == "-ARGCOLORBG-":
            print(">>win/create - button bg: ", values["-ARGCOLORBG-"])
            workspace_window["-ADDCOLORBG-"].update(disabled = False)
        # define line width
        elif event == "-ARGLINEW-":
            print(">>win/create - Line width: ", values["-ARGLINEW-"])
            workspace_window["-ADDLINEW-"].update(disabled = False)
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            color1 = workspace_window["-graph-"].draw_line((-0.50, -0.50), (0.50, -0.50), color = "red", width = App_Functions.get_width(ListOfWidth.index(values["-ARGLINEW-"])))


        # draw a line
        elif event == "-ARGLINETM-" and values["-ARGLINETM-"]:
            try:
                #check if argument is an integer
                is_a_int = int(values["-ARGLINETM-"])
                if App_Functions.check_value(is_a_int, "-ARGLINETM-", workspace_window):
                    print("win/create - Line time - test is an int:", is_a_int)
                    workspace_window["-ARGLINEX1-"].update(disabled = False, value = " ")
            except:
                if len(values["-ARGLINETM-"]) == 1: 
                    continue
                workspace_window["-ARGLINETM-"].update(values["-ARGLINETM-"][:-1])  
        # enable draw a line arguments
        elif event == "-ARGLINEX1-" and values["-ARGLINEX1-"]:
            try:
                #check if argument is an integer
                is_a_floatx1 = float(values["-ARGLINEX1-"])
                if App_Functions.check_value(is_a_floatx1, "-ARGLINEX1-", workspace_window):
                    print("win/create - Line x1 - test is an float:", is_a_floatx1)
                    workspace_window["-ARGLINEY1-"].update(disabled = False, value = " ")
            except:
                if len(values["-ARGLINEX1-"]) == 1 and values["-ARGLINEX1-"][0] == "-": 
                    continue
                workspace_window["-ARGLINEX1-"].update(values["-ARGLINEX1-"][:-1])  
        elif event == "-ARGLINEY1-" and values["-ARGLINEY1-"]:
            try:
                #check if argument is an integer
                is_a_floaty1 = float(values["-ARGLINEY1-"])
                if App_Functions.check_value(is_a_floaty1, "-ARGLINEY1-", workspace_window):
                    print("win/create - Line y1 - test is an float:", is_a_floaty1)
                    workspace_window["-ARGLINEX2-"].update(disabled = False, value = " ")
            except:
                if len(values["-ARGLINEY1-"]) == 1 and values["-ARGLINEY1-"][0] == "-": 
                    continue
                workspace_window["-ARGLINEY1-"].update(values["-ARGLINEY1-"][:-1])  #slice the list starting from index 0 to the end
        elif event == "-ARGLINEX2-" and values["-ARGLINEX2-"]:
            try:
                #check if argument is an integer
                is_a_floatx2 = float(values["-ARGLINEX2-"])
                if App_Functions.check_value(is_a_floatx2, "-ARGLINEX2-", workspace_window):
                    print("win/create - Line x2 - test is an float:", is_a_floatx2)
                    workspace_window["-ARGLINEY2-"].update(disabled = False, value = " ")
            except:
                if len(values["-ARGLINEX2-"]) == 1 and values["-ARGLINEX2-"][0] == "-": 
                    continue
                workspace_window["-ARGLINEX2-"].update(values["-ARGLINEX2-"][:-1])
        elif event == "-ARGLINEY2-" and values["-ARGLINEY2-"]:
            try:
                #check if argument is an integer
                is_a_floaty2 = float(values["-ARGLINEY2-"])
                if App_Functions.check_value(is_a_floaty2, "-ARGLINEY2-", workspace_window):
                    print("win/create - Line y2 - test all floats:", is_a_floatx1, is_a_floaty1, is_a_floatx2, is_a_floaty2)
                    App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
                    color2 = workspace_window["-graph-"].draw_line((is_a_floatx1, is_a_floaty1), (is_a_floatx2, is_a_floaty2), color = "magenta", width = 2)            
                    workspace_window["-ADDLINE-"].update(disabled = False)
            except:
                if len(values["-ARGLINEY2-"]) == 1 and values["-ARGLINEY2-"][0] == "-": 
                    continue
                workspace_window["-ARGLINEY2-"].update(values["-ARGLINEY2-"][:-1])




        # draw an oval/circle
        elif event == "-ARGOVALTM-" and values["-ARGOVALTM-"]:
            try:
                #check if argument is an integer
                is_a_int = int(values["-ARGOVALTM-"])
                if App_Functions.check_value(is_a_int, "-ARGOVALTM-", workspace_window):
                    print("win/create - oval time - test is a int:", is_a_int)
                    workspace_window["-ARGOVALX-"].update(disabled = False, value = " ")
            except:
                if len(values["-ARGOVALTM-"]) == 1: 
                    continue
                workspace_window["-ARGOVALTM-"].update(values["-ARGOVALTM-"][:-1])  
        # enable draw an oval arguments
        elif event == "-ARGOVALX-" and values["-ARGOVALX-"]:
            try:
                #check if argument is a float
                is_a_floatx = float(values["-ARGOVALX-"])
                if App_Functions.check_value(is_a_floatx, "-ARGOVALX-", workspace_window):
                    print("win/create - Oval x - test is a float:", is_a_floatx)
                    App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
                    #color2 = workspace_window["-graph-"].draw_circle((0.5, 0.5), line_color = "magenta", line_width = 2)            
                    workspace_window["-ARGOVALY-"].update(disabled = False, value = " ")
                    workspace_window["-ADDOVAL-"].update(disabled = False)
            except:
                if len(values["-ARGOVALX-"]) == 1 and values["-ARGOVALX-"][0] == "-": 
                    continue
                workspace_window["-ARGOVALX-"].update(values["-ARGOVALX-"][:-1])
        elif event == "-ARGOVALY-" and values["-ARGOVALY-"]:
            try:
                #check if argument is a float
                is_a_floaty = float(values["-ARGOVALY-"])
                if App_Functions.check_value(is_a_floaty, "-ARGOVALY-", workspace_window):
                    print("win/create - Oval y - test all floats:", is_a_floatx, is_a_floaty)
                    App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
                    #color3 = workspace_window["-graph-"].draw_oval((0.5, 0.5), line_color = "magenta", line_width = 2)            
            except:
                if len(values["-ARGOVALY-"]) == 1 and values["-ARGOVALY-"][0] == "-": 
                    continue
                workspace_window["-ARGOVALY-"].update(values["-ARGOVALY-"][:-1])

         
            

       

 
        elif event == "-ADDLINE-":
            #sets the SCRIPT section
            list_script_temp.append(values["-ARGLINETM-"])
            list_script_temp.append(float(values["-ARGLINEX1-"]))
            list_script_temp.append(float(values["-ARGLINEY1-"]))
            list_script_temp.append(float(values["-ARGLINEX2-"]))
            list_script_temp.append(float(values["-ARGLINEY2-"]))
            list_of_script.append(list_script_temp.copy())
            workspace_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(values["-ARGLINETM-"])
            list_text_temp.append(values["-ARGLINEX1-"])
            list_text_temp.append(values["-ARGLINEY1-"])
            list_text_temp.append(values["-ARGLINEX2-"])
            list_text_temp.append(values["-ARGLINEY2-"])
            list_of_text = " ".join(list_text_temp)
            workspace_window["-FILE_TEXT-"].write(list_of_text + "\n")
            print(">>win/create - cursorp - list of script: ", list_of_script)
            print(">>win/create - cursorp - list of text: ", list_of_text)
            #clear layout enviroment
            workspace_window["-CURSORP-"].reset_group()
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            App_Functions.clear_fields(workspace_window)
        elif event == "-ADDOVAL-":
            #sets the SCRIPT section
            list_script_temp.append(values["-ARGOVALTM-"])
            list_script_temp.append(values["-ARGOVALX-"])
            try:
                if len(values["-ARGOVALY-"]) != 0:
                    list_script_temp.append(values["-ARGOVALY-"])
            except:
                continue
            list_of_script.append(list_script_temp.copy())
            workspace_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(values["-ARGOVALTM-"])
            list_text_temp.append(values["-ARGOVALX-"])
            list_text_temp.append(values["-ARGOVALY-"])
            list_of_text = " ".join(list_text_temp)
            workspace_window["-FILE_TEXT-"].write(list_of_text + "\n")
            print(">>win/create - cursorp - list of script: ", list_of_script)
            print(">>win/create - cursorp - list of text: ", list_of_text)
            #clear layout enviroment
            workspace_window["-CURSORP-"].reset_group()
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            App_Functions.clear_fields(workspace_window) 



        elif event == "-ADDCLEAR-":
            #sets the SCRIPT section
            list_of_script.append(list_script_temp.copy())
            workspace_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_of_text = " ".join(list_text_temp)
            workspace_window["-FILE_TEXT-"].write(list_of_text + "\n")
            print(">>win/create - clear - list of script: ", list_of_script)
            print(">>win/create - clear - list of text: ", list_of_text)
            #clear layout enviroment
            workspace_window["-CLEAR-"].reset_group()
            App_Functions.clear_fields(workspace_window)
        elif event == "-ADDCLEARL-":
            print("ARGCLEARL value: ", (values["-ARGCLEARL-"]))
            #sets the SCRIPT section
            try:
                if len(values["-ARGCLEARL-"]) != 0:
                    list_script_temp.append(values["-ARGCLEARL-"])
            except:
                continue
            list_of_script.append(list_script_temp.copy())
            workspace_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            try:
                if len(values["-ARGCLEARL-"]) != 0:
                    list_text_temp.append(values["-ARGCLEARL-"])
            except:
                continue
            list_of_text = " ".join(list_text_temp)
            workspace_window["-FILE_TEXT-"].write(list_of_text + "\n")
            print(">>win/create - font size - list of script: ", list_of_script)
            print(">>win/create - font size - list of text: ", list_of_text)
            #clear layout enviroment
            workspace_window["-CLEAR-"].reset_group()
            App_Functions.clear_fields(workspace_window)
        elif event == "-A-":
            print ("add test SPIN: ", values["-ARGA-"], values["-ARGB-"])
            #sets the SCRIPT section
            list_script_temp.append(str(values["-ARGA-"]))
            list_script_temp.append(str(values["-ARGB-"]))
            list_of_script.append(list_script_temp.copy())
            workspace_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(str(values["-ARGA-"]))
            list_text_temp.append(str(values["-ARGB-"]))
            list_of_text = " ".join(list_text_temp)
            workspace_window["-FILE_TEXT-"].write(list_of_text + "\n")
            print(">>win/create - cursorp - list of script: ", list_of_script)
            print(">>win/create - cursorp - list of text: ", list_of_text)
            #clear layout enviroment
            workspace_window["-CURSORP-"].reset_group()
            App_Functions.clear_image(workspace_window, color1, color2, color3, color4, color5, color6, color7, color8)
            App_Functions.clear_fields(workspace_window)
     

       
 
       
        
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



