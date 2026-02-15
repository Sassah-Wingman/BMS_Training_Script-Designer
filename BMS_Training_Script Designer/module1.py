import PySimpleGUI as sg
import Script_Images
import Script_Functions

alignleft = sg.TEXT_LOCATION_LEFT


def create_window():
    #graph global variables
    colort = None
    colorb = None
    colorbg = None
    colortxbg = None
    colortx = None
    

    #empty lists
    list_script_temp = []
    list_text_temp = []
    list_of_script = []
    list_of_text = []
    ListOfColors = ["Red", "Yellow", "Cyan", "Magenta","Green1", "Black", "White"]
           
    create_tooltips = ["a", "b"]
    
    tab_script = [[sg.Radio("Add a comment line to your script >>>", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-COMMENT-"), 
                   sg.Input(" ", size = (30), enable_events = True, disabled = True, disabled_readonly_background_color = "gray", key = "-ARGCOMMENT-"), 
                   sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False,  disabled = True, key = "-ADDCOMMENT-")],
                  [sg.Radio("Add a blank line >", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-LINE-"), 
                   sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDLINE-")],
                  [sg.Radio("Set the text color >>>", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-COLORT-"), 
                   sg.Combo(values = ListOfColors, size = (10, 1), background_color = "gray", readonly = True, enable_events = True,  disabled = True, key = "-ARGCOLORT-"),
                   sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDCOLORT-")],
                  [sg.Radio("Set the background color >>>", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-COLORB-"), 
                   sg.Combo(values = ListOfColors, size = (10, 1), background_color = "gray", readonly = True, enable_events = True,  disabled = True, key = "-ARGCOLORB-"),
                   sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDCOLORB-")],
                  [sg.Radio("Turn your text background ON/OFF>", circle_color = "#ffffff", group_id = 1, enable_events = True, disabled = True, key = "-COLORBG-"),
                   sg.Spin(values = ("ON", "OFF"), initial_value = "OFF", size = (6), enable_events = True, wrap = True, disabled = True, key = "-ARGCOLORBG-"),
                   sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDCOLORBG-")],
                  [sg.Radio("Set text to flash >>>", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-FLASHT-"),
                   sg.Text("Disabled", text_color = "#ffffff", font = "_ 11"),
                   sg.Slider(range = (0, 9), default_value = 0, tick_interval = 1, size = (30, 8), font = "_ 11", orientation = "h", resolution = 1, enable_events = True, disabled = True, key = "-ARGFLASHT-"),
                   sg.Text("Max rate", text_color = "#ffffff", font = "_ 11"),
                   sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDFLASHT-")],
                  
                  [sg.Radio("Change font size", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-FONT-"), sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDFONT-")],
                  [sg.Radio("Change text justification", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-JUST-"), sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDJUST-")],
                  [sg.Radio("Set the cursor initial position", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-CURSORP-"), sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDCURSORP-")],
                  [sg.Radio("Move cursor from its present position", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-CURSORM-"), sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDCURSORM-")],
                  [sg.Radio("Display a text on screen for a time", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-PRINT-"), sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDPRINT-")],
                  [sg.Radio("Display a text on screen while pausing the script", circle_color = "#ffffff", group_id = 1, enable_events = True, key = "-PRINTP-"), sg.Push(), sg.Button(button_text = "Add", size = (8), font = "_ 12", visible = False, key = "-ADDPRINTP-")],]
    
    tab_text = [[sg.Radio("a", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],
                [sg.Radio("b", group_id = 1, key = "-FONTCOLOR-")],
                [sg.Radio("c", group_id = 1, key = "-FONTBACK-")],
                [sg.Radio("d", group_id = 1, key = "-FONTFLASH-")]]
    
    tab_draw = [[sg.Radio("e", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],
                [sg.Radio("f", group_id = 1, key = "-FONTCOLOR-")],
                [sg.Radio("g", group_id = 1, key = "-FONTBACK-")],
                [sg.Radio("h", group_id = 1, key = "-FONTFLASH-")]]

    tab_time = [[sg.Radio("i", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],
                [sg.Radio("j", group_id = 1, key = "-FONTCOLOR-")],
                [sg.Radio("k", group_id = 1, key = "-FONTBACK-")],
                [sg.Radio("l", group_id = 1, key = "-FONTFLASH-")]]
    
    tab_aircraft = [[sg.Radio("Block", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],
                    [sg.Radio("Allow", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("Pan Tilt", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("Move Pan Tilt", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("Hilite 3d Radio", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("SIm Command", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("Sim command press", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("Sim command release", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("Set fault", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("clear fault", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("set mav cool time", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")], 
                    [sg.Radio("set gun ammo", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],
                    [sg.Radio("set fuel", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],]
                    

    
    tab_condition = [[sg.Radio("5", circle_color = "#ffffff", group_id = 1, key = "-FONTSIZE-")],
                     [sg.Radio("6", group_id = 1, key = "-FONTCOLOR-")],
                     [sg.Radio("7", group_id = 1, key = "-FONTBACK-")],
                     [sg.Radio("8", group_id = 1, key = "-FONTFLASH-")],]

    function_col = sg.Frame("Script Functions:", [[sg.TabGroup([[sg.Tab(" Global Functions ", tab_script),
                                                   sg.Tab(" Text Functions ", tab_text),
                                                   sg.Tab(" Shapes Functions ", tab_draw), 
                                                   sg.Tab(" Wait Triggers ", tab_time), 
                                                   sg.Tab(" Aircraft Configuration ", tab_aircraft), 
                                                   sg.Tab(" Conditionals ", tab_condition)],], 
                             font = "_ 12")],
                             [sg.Text("What this function does: ", font = "_ 11", background_color = "#64778d",), 
                              sg.Text(" ", font = "_ 11", background_color = "#64778d", text_color = ("yellow"), key = "-DESC-")],
                             [sg.Text("What You must provide: ", font = "_ 11", background_color = "#64778d"), 
                              sg.Text(" ", font = "_ 11", background_color = "#64778d", text_color = ("gold2"), key = "-SYNT-")],
                             [sg.Text("Tips how to use it: ", font = "_ 11", background_color = "#64778d"), 
                              sg.Text(" ", font = "_ 11", background_color = "#64778d", text_color = ("bisque"), key = "-EXEM-")],
                             [sg.Button("1"), sg.Button("2"), sg.Button("3")]],
                             title_color = "#ffffff", background_color = "#64778d", size = (800, 670), vertical_alignment = "top")

    graph_col = sg.Frame("Graphic Representation:", [[sg.Graph((1000, 570), (-1,-1), (1, 1), background_color = "black", key = "-graph-")],   #1000, 570
                                                     [sg.Push(), sg.Text(">>> Graphic samples may not match the one in game. <<<", background_color = "#64778d", text_color = "yellow", key = "-TST-"), sg.Push()], 
                                                     [sg.Push(), sg.Checkbox("Show grid.", background_color = "#64778d", default = False, enable_events = True,  key = "-GRID-"), 
                                                      sg.Checkbox("Show shapes.", background_color = "#64778d", default = False, enable_events = True,  key = "-SHAPE-"), 
                                                      sg.Radio("Show cockpit1.", "RADIO1", background_color = "#64778d", default = False, enable_events = True,  key = "-CKPT1-"),
                                                      sg.Radio("Show cockpit2.", "RADIO1", background_color = "#64778d", default = False, enable_events = True,  key = "-CKPT2-"),
                                                      sg.Radio("Show cockpit3.", "RADIO1", background_color = "#64778d", default = False, enable_events = True,  key = "-CKPT3-"), sg.Push()]],
                         title_color = "#ffffff", background_color = "#64778d", vertical_alignment = "top")

    headings = ["Function", "1st Argument", "2nd Argument", "3rd Argument", "4th Argument", "5th Argument"]

    script_col = sg.Frame("Script:", [[sg.Table(list_of_script,
                                                font = ("_, 10"),
                                                headings = headings,
                                                header_font = ("_, 10"),
                                                header_background_color = "#91a6be",
                                                def_col_width = 25,
                                                background_color = "#d4d7dd",
                                                alternating_row_color = "#ffffff",
                                                auto_size_columns = False,
                                                display_row_numbers = True,
                                                starting_row_number = 1,
                                                selected_row_colors = ("#ffffff", "#64778d"),
                                                size = (1410, 260),
                                                justification = "left", 
                                                key = "-SCRIPT-",)]], 
                          title_color = "#ffffff", background_color = "#64778d", size = (1415, 270), vertical_alignment = "top")
    
    
    summary_col = sg.Frame("Script Summary:", [[sg.Multiline(auto_refresh = True,
                                                            font = ("_, 10"),
                                                            background_color = "light gray",
                                                            size = (200,260),
                                                            justification = "left",
                                                            wrap_lines = True,
                                                            key = "-TEXT-",)]], 
                         title_color = "#ffffff", background_color = "#64778d", size = (400, 270), vertical_alignment = "top")

    status_col = sg.StatusBar(text = "Tips will be shown here!                                                                                                                                                                                                                                                                          ",                               
                              text_color = "#ffffff", 
                              justification = "left", 
                              auto_size_text = True, 
                              expand_x = True, 
                              key = "-STATUS-")
    
    
    layout = [[function_col, graph_col], 
              [script_col, summary_col], 
              [status_col]]
       
                                            

    create_window = sg.Window("Create Script", 
                            layout, 
                            icon = Script_Images.start_icon, 
                            return_keyboard_events = False, 
                            finalize = True, 
                            resizable = True,
                            auto_save_location = True,
                            modal = True,
                            location = (50, 50), 
                            size = (1820, 900))

    ckpt_image1 = create_window["-graph-"].draw_image(data = Script_Images.cockpit_image1, location = (-1, 1))

    target_img = create_window["-graph-"].draw_image(data = Script_Images.target_image, location = (0, 0))

    bpressed = True

    while True:
        
        event, values = create_window.read()
        print(">>WIN/CREATE - events: ", event)

        
        if event in (sg.WIN_CLOSED, "-quit-"):
            print(">>win/create - event: exit")
            break

        #enable functions settings
        #add comments
        if event == "-COMMENT-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
            create_window["-DESC-"].update("Add a line that will be ignored by the script.")
            create_window["-SYNT-"].update("Just write anything you want.")
            create_window["-EXEM-"].update("It is important to comment your script. At least an introduction about what it does.")
            create_window["-STATUS-"].update(value = "It is good practice to explain what each section of your script does.")
            create_window["-ADDCOMMENT-"].update(visible = True)
            create_window["-ARGCOMMENT-"].update(visible = True, disabled = False)
            create_window["-ARGCOMMENT-"].set_focus(force = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("//")
            list_text_temp.append("Comment:  ")
            print(">>win/create - comment - list functemp script: ", list_script_temp)
            print(">>win/create - comment - list functemp text: ", list_text_temp)
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
        #add space line
        elif event == "-LINE-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
            create_window["-ADDLINE-"].update(disabled = False)
            create_window["-DESC-"].update("Add an empty line to separate different sections of the script.")
            create_window["-SYNT-"].update("Nothing.")
            create_window["-EXEM-"].update("Separate parts of your script using space to help it became more readble.")
            create_window["-STATUS-"].update(value = "Leave spaces between blocks of scpripts to help the organization.")
            create_window["-ADDLINE-"].update(visible = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("\n")
            list_text_temp.append(" ")
            print(">>win/create - space line - list functemp script: ", list_script_temp)
            print(">>win/create - space line - list functemp text: ", list_text_temp)
            print(">>win/create - space line - list of script: ", list_of_script)
            print(">>win/create - space line - list of text: ", list_of_text)
        #adjust text color
        elif event == "-COLORT-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
            create_window["-DESC-"].update("Sets the color of the text.")
            create_window["-SYNT-"].update("Pick a color.")
            create_window["-EXEM-"].update("Use different colors to diferent context.")
            create_window["-STATUS-"].update(value = "The setting affects all following text functions until another color is defined.")
            create_window["-ADDCOLORT-"].update(visible = True)
            create_window["-ARGCOLORT-"].update(disabled = False, background_color = "#ffffff")
            create_window["-ARGCOLORT-"].set_focus(force = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("SetFontColor")
            list_text_temp.append("Text Color: ")
            print(">>win/create - Font Color - list functemp script: ", list_script_temp)
            print(">>win/create - Font Color - list functemp text: ", list_text_temp)
            print(">>win/create - Font Color - list of script: ", list_of_script)
            print(">>win/create - Font Color - list of text: ", list_of_text)
        #adjust background text color
        elif event == "-COLORB-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
            create_window["-DESC-"].update("Sets the background color of the text. The default is transparent.")
            create_window["-SYNT-"].update("Pick a color.")
            create_window["-EXEM-"].update("Use background colors to highlight important information.")
            create_window["-STATUS-"].update(value = "You must turn <Box your Text> ON or OFF in order to activate/deactivate text background.")
            create_window["-ADDCOLORB-"].update(visible = True)
            create_window["-ARGCOLORB-"].update(disabled = False, background_color = "#ffffff")
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("SetFontBGColor")
            list_text_temp.append("Boxed Text Color: ")
            print(">>win/create - Font Color - list functemp script: ", list_script_temp)
            print(">>win/create - Font Color - list functemp text: ", list_text_temp)
            print(">>win/create - Font Color - list of script: ", list_of_script)
            print(">>win/create - Font Color - list of text: ", list_of_text)
        #enable background text color
        elif event == "-COLORBG-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
            create_window["-DESC-"].update("Turn on and off the background color of the text.")
            create_window["-SYNT-"].update("None.")
            create_window["-EXEM-"].update("You can set the text color first and turn background ON and OFF along the script.")
            create_window["-STATUS-"].update(value = "This function affects all print functions until another value is defined. You have to define a background color first.")
            create_window["-ARGCOLORBG-"].update(visible = True, disabled = False)
            create_window["-ADDCOLORBG-"].update(visible = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("SetTextBoxed")
            list_text_temp.append("Text background color turned: ")
            print(">>win/create - Font Color - list functemp script: ", list_script_temp)
            print(">>win/create - Font Color - list functemp text: ", list_text_temp)
            print(">>win/create - Font Color - list of script: ", list_of_script)
            print(">>win/create - Font Color - list of text: ", list_of_text)
        elif event == "-FLASHT-":
            list_script_temp.clear()
            list_text_temp.clear()
            #reset workspace layout
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
            create_window["-DESC-"].update("Sets the rate of flashing that should occur for all text functions.")
            create_window["-SYNT-"].update("Adjust flash rating from none (0ms) to the hightest frequency (900ms).")
            create_window["-EXEM-"].update("Flashing can make the reading text somewhat tiresome.  Use it with caution.")
            create_window["-STATUS-"].update(value = "The setting affects all following text functions until another value is defined.")
            create_window["-ARGFLASHT-"].update(visible = True, disabled = False)
            create_window["-ADDFLASHT-"].update(visible = True)
            #configure SCRIPT and SUMMARY input
            list_script_temp.append("SetFontFlash")
            list_text_temp.append("Flashing text rate:  ")
            print(">>win/create - comment - list functemp script: ", list_script_temp)
            print(">>win/create - comment - list functemp text: ", list_text_temp)
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)

             


        # elif event == "-CURSORP-":
        #     Script_Functions.clear_functions(create_window)
        #     list_script_temporary.clear()
        #     list_text_temporary.clear()
        #     print(">>win/create - cursor position")
        #     #configure workspace layout
        #     create_window["-DESC-"].update("Sets the cursor to the specified position.")
        #     create_window["-SYNT-"].update("Two float numbers: <float (x)> <float (y)>. Range from -1.00 to 1.00.")
        #     create_window["-EXEM-"].update("SetCursor -0.04 0.8")
        #     create_window["-STATUS-"].update(value = "A good position to start your text is:  -0.04(x) 0.00(y)")
        #     create_window["-ARGTXT2-"].update("Set axis X position: ")
        #     create_window["-ARGTXT3-"].update("Set axis Y position: ")
        #     create_window["-ARG2-"].update(visible = True)
        #     create_window["-ARG3-"].update(visible = True)
        #     #target_img = create_window["-graph-"].draw_image(data = Script_Images.target_image, location = (0, 0))            #configure function input
        #     list_script_temporary.append("SetCursor")
        #     list_text_temporary.append("Cursor position (x/y): ")




        #add functions settings to the script
        if event == "-ADDCOMMENT-":
            #sets the SCRIPT section
            list_script_temp.append(values["-ARGCOMMENT-"])
            list_of_script.append(list_script_temp.copy())
            create_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(values["-ARGCOMMENT-"])
            list_of_text = " ".join(list_text_temp)
            create_window["-TEXT-"].write(list_of_text + "\n")
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
            #clear layout enviroment
            create_window["-COLORT-"].reset_group()
            Script_Functions.clear_fields(create_window)
        elif event == "-ADDLINE-":
            #sets the SCRIPT section
            list_of_script.append(list_script_temp.copy())
            create_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_of_text = " ".join(list_text_temp)
            create_window["-TEXT-"].write(list_of_text + "\n")
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
            #clear layout enviroment
            create_window["-COLORT-"].reset_group()
            Script_Functions.clear_fields(create_window)
        elif event == "-ADDCOLORT-":
            #sets the SCRIPT section
            list_script_temp.append(Script_Functions.get_color_hex(ListOfColors.index(values["-ARGCOLORT-"])))
            list_of_script.append(list_script_temp.copy())
            create_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(values["-ARGCOLORT-"])
            list_of_text = " ".join(list_text_temp)
            create_window["-TEXT-"].write(list_of_text + "\n")
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
            #clear layout enviroment
            create_window["-COLORT-"].reset_group()
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
        elif event == "-ADDCOLORB-":
            #sets the SCRIPT section
            list_script_temp.append(Script_Functions.get_color_hex(ListOfColors.index(values["-ARGCOLORB-"])))
            list_of_script.append(list_script_temp.copy())
            create_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(values["-ARGCOLORB-"])
            list_of_text = " ".join(list_text_temp)
            create_window["-TEXT-"].write(list_of_text + "\n")
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
            #clear layout enviroment
            create_window["-COLORB-"].update(disabled = False)
            create_window["-COLORBG-"].update(disabled = False)
            bgcolor = values["-ARGCOLORT-"]
            create_window["-COLORB-"].reset_group()
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
        elif event == "-ADDCOLORBG-":
            print("ARGCOLORBG value: ", values["-ARGCOLORBG-"])
            #sets the SCRIPT section
            list_script_temp.append(Script_Functions.get_On_Off(values["-ARGCOLORBG-"]))
            list_of_script.append(list_script_temp.copy())
            create_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(values["-ARGCOLORBG-"])
            list_of_text = " ".join(list_text_temp)
            create_window["-TEXT-"].write(list_of_text + "\n")
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
            #clear layout enviroment
            create_window["-COLORBG-"].reset_group()
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)
        elif event == "-ADDFLASHT-":
            print("ARGFLASHT value: ", values["-ARGFLASHT-"])
            #sets the SCRIPT section
            list_script_temp.append(Script_Functions.get_flash_hex(values["-ARGFLASHT-"]))
            list_of_script.append(list_script_temp.copy())
            create_window["-SCRIPT-"].update(values = list_of_script)
            #sets the SUMMARY section
            list_text_temp.append(str(values["-ARGFLASHT-"]))
            list_of_text = " ".join(list_text_temp)
            create_window["-TEXT-"].write(list_of_text + "\n")
            print(">>win/create - comment - list of script: ", list_of_script)
            print(">>win/create - comment - list of text: ", list_of_text)
            #clear layout enviroment
            create_window["-FLASHT-"].reset_group()
            Script_Functions.clear_image(create_window, colorb, colort, colortx, colortxbg, colorbg)
            Script_Functions.clear_fields(create_window)

      

        #configure events
        #edit comment
        if event == "-ARGCOMMENT-":
            print(">>win/create - inputc comment: ", values["-ARGCOMMENT-"])
            create_window["-ADDCOMMENT-"].update(disabled = False)
        #edit text color
        elif event == "-ARGCOLORT-" and values["-ARGCOLORT-"] in ListOfColors:
            print(">>win/create - combo colort: ", values["-ARGCOLORT-"])
            create_window["-ADDCOLORT-"].update(disabled = False)
            colort = create_window["-graph-"].draw_text("This is the color of your text!", (-0.75, 0.0), color = values["-ARGCOLORT-"], font = "arial 12 bold")
        #edit background text color
        elif event == "-ARGCOLORB-" and values["-ARGCOLORB-"] in ListOfColors:   
            print(">>win/create - combo colorb: ", values["-ARGCOLORB-"])
            create_window["-ARGCOLORT-"].update(disabled = False, background_color = "#ffffff")
            create_window["-COLORT-"].update(text = "Test a text over background >>>", disabled = True)
            create_window["-ADDCOLORB-"].update(disabled = False)
            colorb = create_window["-graph-"].draw_rectangle((-0.98, 0.03), (-0.50, -0.03), fill_color = values["-ARGCOLORB-"], line_color = values["-ARGCOLORB-"]) 
        elif event == "-ARGCOLORBG-":
            #print(">>win/create - button bg: ", values["-ARGCOLORBG-"])
            create_window["-ADDCOLORBG-"].update(disabled = False)
        elif event == "-ARGFLASHT-":
            print(">>win/create - slider flash: ", values["-ARGFLASHT-"])
            create_window["-ADDFLASHT-"].update(disabled = False)
            colort = create_window["-graph-"].draw_text("Flashing sample will be added soon!", (-0.75, 0.0), color = "yellow", font = "arial 12 bold")
       
 
        # if event == "-ARG2-" or "-ARG3-":
        #      if values["-CURSORP-"] == True:
        #          #target_img = create_window["-graph-"].draw_image(data = Script_Images.target_image, location = (0, 0))            #configure function input
        #          create_window["-graph-"].relocate_figure(figure = target_img, x = (values["-ARG2-"]),  y = (values["-ARG3-"]))
        #          print("position x: ", values["-ARG2-"])
        #          print("position y: ", values["-ARG3-"])
        #          string2 = str(values["-ARG2-"])
        #          string3 = str(values["-ARG3-"])
        #          print("string 1: ", type(string2))
        #          print("string 2: ", type(string3))
        #          create_window["-ADD-"].update(disabled = False)
        #          create_window["-CLEAR-"].update(disabled = False)
        #      else:
        #          create_window["-graph-"].delete_figure(target_img)

        
        if event == "-GRID-":
            print(">>win/create - values in GRID: ", values["-GRID-"])
            if values["-GRID-"] == True:
                #draw vertical and horizontal lines
                line1 = create_window["-graph-"].draw_line((0.50, 1), (0.50, -1), color = "yellow", width = 1)
                line2 = create_window["-graph-"].draw_line((-0.50, 1), (-0.50, -1), color = "yellow", width = 1)
                line3 = create_window["-graph-"].draw_line((1, 0.50), (-1, 0.50), color = "yellow", width = 1)
                line4 = create_window["-graph-"].draw_line((1, -0.50), (-1, -0.50), color = "yellow", width = 1)
                line5 = create_window["-graph-"].draw_line((0,1), (0, -1), color = "yellow", width = 3)
                line6 = create_window["-graph-"].draw_line((1,0), (-1, 0), color = "yellow", width = 3)
                line7 = create_window["-graph-"].draw_line((0.51, -0.60), (0.51, -0.40), color = "yellow", width = 1)
                line8 = create_window["-graph-"].draw_line((0.60, -0.51), (0.40, -0.51), color = "yellow", width = 1)
                print(">>win/create - lines id: ", line1, line2, line3, line4, line5, line6, line7, line8)
                
                #Display coordinates
                coord1 = create_window["-graph-"].draw_text("0.0   0.0", (0, 0.03), color = "yellow", font = "arial 12 bold")
                coord2 = create_window["-graph-"].draw_text("-1.0 / 1.0", (-0.92, 0.95), color = "yellow", font = "arial 12 bold")
                coord3 = create_window["-graph-"].draw_text("-1.0 / -1.0", (-0.92, -0.95), color = "yellow", font = "arial 12 bold")
                coord4 = create_window["-graph-"].draw_text(" 1.0 / 1.0", (0.92, 0.95), color = "yellow", font = "arial 12 bold")
                coord5 = create_window["-graph-"].draw_text(" 1.0 / -1.0", (0.92, -0.95), color = "yellow", font = "arial 12 bold")
                coord6 = create_window["-graph-"].draw_text("0.01 interval", (0.63, -0.55), color = "yellow", font = "arial 12 bold")
                print(">>win/create - coord id: ", coord1, coord2, coord3, coord4, coord5, coord6)
            else:
                #delete lines
                create_window["-graph-"].delete_figure(line1)
                create_window["-graph-"].delete_figure(line2)
                create_window["-graph-"].delete_figure(line3)
                create_window["-graph-"].delete_figure(line4)
                create_window["-graph-"].delete_figure(line5)
                create_window["-graph-"].delete_figure(line6)
                create_window["-graph-"].delete_figure(line7)
                create_window["-graph-"].delete_figure(line8)
                #delete coordinates
                create_window["-graph-"].delete_figure(coord1)
                create_window["-graph-"].delete_figure(coord2)
                create_window["-graph-"].delete_figure(coord3)
                create_window["-graph-"].delete_figure(coord4)
                create_window["-graph-"].delete_figure(coord5)
                create_window["-graph-"].delete_figure(coord6)
                
        if event == "-CKPT1-":
            if values["-CKPT1-"] == True:
                print(">>win/create - values in CKPT2: ", values["-CKPT1-"])
                #create_window["-graph-"].erase()
                create_window["-graph-"].delete_figure(ckpt_image2)
                create_window["-GRID-"].update(False)
                ckpt_image1 = create_window["-graph-"].draw_image(data = Script_Images.cockpit_image1, location = (-1, 1))
                print(">>win/create - cockpit image id:", ckpt_image1)
            else:
                create_window["-graph-"].delete_figure(ckpt_image1)

        if event == "-CKPT2-":
            if values["-CKPT2-"] == True:
                print(">>win/create - values in CKPT2: ", values["-CKPT2-"])
                #create_window["-graph-"].erase()
                create_window["-GRID-"].update(False)
                ckpt_image2 = create_window["-graph-"].draw_image(data = Script_Images.cockpit_image2, location = (-1, 1))
                print(">>win/create - cockpit image id:", ckpt_image2)
            else:
                create_window["-graph-"].delete_figure(ckpt_image2)

        if event == "-CKPT3-":
            if values["-CKPT3-"] == True:
                print(">>win/create - values in CKPT3: ", values["-CKPT3-"])
                #create_window["-graph-"].erase()
                create_window["-GRID-"].update(False)
                ckpt_image3 = create_window["-graph-"].draw_image(data = Script_Images.cockpit_image3, location = (-1, 1))
                print(">>win/create - cockpit image id:", ckpt_image3)
            else:
                create_window["-graph-"].delete_figure(ckpt_image3)

        if event == "-SHAPE-":
            print(">>win/create - values in SHAPED: ", values["-SHAPE-"])
            if values["-SHAPE-"] == True:
                #draw lines, circles and retangules
                shape1 = create_window["-graph-"].draw_circle((0.50, 0.50), radius = 0.1, line_color = "red", line_width = 2)
                shape2 = create_window["-graph-"].draw_circle((0.50, 0.50), radius = 0.05, line_color = "red", line_width = 2)
                shape3 = create_window["-graph-"].draw_oval((0.50, 0.50), (0.25, 0.25), line_color = "red", line_width = 2)
                shape4 = create_window["-graph-"].draw_rectangle((0.50, 0.50), (0.25, 0.25), line_color = "red", line_width = 2)
                shape5 = create_window["-graph-"].draw_line((-0.50, -0.50), (-0.25, -0.25), color = "red", width = 2)
                shape6 = create_window["-graph-"].draw_text("this is a line", (-0.80, -0.04), font = "arial 8",  color = "red", text_location = alignleft)
                shape7 = create_window["-graph-"].draw_rectangle((-0.80, -0.07), (-0.60, -0.10), fill_color = "white", line_color = "white", line_width = 2)
                shape8 = create_window["-graph-"].draw_text("this is another line", (-0.80, -0.08), font = "arial 8",  color = "red", text_location = alignleft)
                
                print(">>win/create - lines id: ", shape1, shape2, shape3, shape4, shape5, shape6, shape7, shape8)
            else:
                create_window["-graph-"].delete_figure(shape1)
                create_window["-graph-"].delete_figure(shape2)
                create_window["-graph-"].delete_figure(shape3)
                create_window["-graph-"].delete_figure(shape4)
                create_window["-graph-"].delete_figure(shape5)
                create_window["-graph-"].delete_figure(shape6)
                create_window["-graph-"].delete_figure(shape7)
                create_window["-graph-"].delete_figure(shape8)



        if event == "-T-":
            #clear arguments window after switching functions selection
            create_window["-ARGTXT1-"].update(" ")
            create_window["-ARGTXT2-"].update(" ")
            create_window["-ARGTXT3-"].update(" ")
            create_window["-ARGTXT4-"].update(" ")
            create_window["-ARGTXT5-"].update(" ")
            create_window["-ARGTXT6-"].update(" ") 
            create_window["-ARGTXT7-"].update(" ")
            create_window["-ARGTXT8-"].update(" ")
            create_window["-ARGTXT9-"].update(" ")
            create_window["-ARGTXT10-"].update(" ")
            create_window["-ARGTXT11-"].update(" ")
            create_window["-ARGTXT12-"].update(" ")
            create_window["-ARGTXT13-"].update(" ")
            create_window["-ARGTXT14-"].update(" ")
            create_window["-ARGCOMMENT-"].update(visible = False)
            create_window["-ARG2-"].update(visible = False)
            create_window["-ARG3-"].update(visible = False)
            create_window["-ARGCOLORT-"].update(visible = False)
            create_window["-ARG5-"].update(visible = False)
            create_window["-ARGCOLORBG-"].update(visible = False)
            create_window["-ARG7-"].update(visible = False)
            create_window["-ARG8-"].update(visible = False)
            create_window["-ARG9-"].update(visible = False)
            create_window["-ARG10-"].update(visible = False)
            create_window["-ARG11-"].update(visible = False)
            create_window["-ARG12-"].update(visible = False)
            create_window["-ARG13-"].update(visible = False)
            create_window["-ARG14-"].update(visible = False)
            create_window["-ADD-"].update(disabled = True)
            create_window["-CLEAR-"].update(disabled = True)










    create_window.close()  
    return create_window

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
            create_window()
        
        if event == "-EDITS-":
            pass

         
    start_window.close()  
    return start_window


