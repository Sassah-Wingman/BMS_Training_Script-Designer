import FreeSimpleGUI as sg
import os
import App_Functions

# Handle delete scripts
def manage_window():

    left_col = sg.Column([[sg.Text("List of Files:")],
                          [sg.Listbox(values = App_Functions.extension_txt(sg.user_settings_get_entry("-setcamppath-")),
                                      enable_events = True, 
                                      size = (30,25),
                                      key="-FILE_LIST-")],], 
                           element_justification = "Left", expand_x = True, expand_y = False, vertical_alignment = "top")

    right_col = sg.Column([[sg.Text(" ", key = "-FILE_NAME-")],
                          [sg.Multiline(size = (100,25),
                                        background_color = "light gray",
                                        text_color = "gray50",
                                        key = "-FILE_TEXT-", 
                                        disabled = True)],], 
                           element_justification = "Left", expand_x = True, expand_y=False, vertical_alignment = "top")
    
    buttons_line = [[sg.Text("Selected File: ", font = "_ 14"), sg.Text(" ", text_color = "#ffffff", key = "-FILE-")],
                    [sg.Push(), sg.Text("Choose the type of file to be displayed.", text_color = "#ffffff", font = "_ 16",), sg.Push()],
                    [sg.Push(), sg.Radio("Show .txt Only", "RADIO1", font = "_ 14", enable_events = True, circle_color = "#ffffff", default =  True, key = "-TXT-"),
                     sg.Radio("Show .run Only", "RADIO1", font = "_ 14", enable_events = True, circle_color = "#ffffff", default = False, key = "-RUN-"), 
                     sg.Radio("Show all Files", "RADIO1", font = "_ 14", enable_events = True, circle_color = "#ffffff", default =  False, key = "-ALL-"), sg.Push()],
                    [sg.Text(" ")],
                    [sg.HorizontalSeparator()],
                    [sg.Push(),sg.Button(button_text = "Edit Script", 
                                         key = "-EDIT_SCPT-",
                                         disabled = True,
                                         size = (16, 1), 
                                         font = "_ 12"),
                    sg.Button(button_text = "Delete Script", 
                              key = "-DEL_SCPT-",
                              disabled = True,
                              button_color = "red",  
                              size = (16, 1), 
                              font = "_ 12"),
                    sg.Button(button_text = "Close", 
                              key = "-CLOSE-", 
                              size = (16, 1), 
                              font = "_ 12"), 
                     sg.Push(),],]

    layout = [[left_col, right_col], [buttons_line]]

    manage_window = sg.Window("Select a File", 
                               layout, 
                               return_keyboard_events = False, 
                               finalize=True, 
                               resizable=True, 
                               keep_on_top = True, 
                               size = (1000, 700))
    
    while True:
        event, values = manage_window.read()
        print("** DELETE SCRIPT WINDOW events: ", event)

        #close convert window
        if event in (None, sg.WIN_CLOSED, "-CLOSE-"):
            print("** DELETE SCRIPT WINDOW - convert window closed.")
            break
        
        manage_window["-FILE_LIST-"].update(App_Functions.extension_to_be_displayed(sg.user_settings_get_entry("-setcamppath-"), values["-TXT-"], values["-RUN-"], values["-ALL-"]))
        manage_window["-FILE_TEXT-"].update(" ")
        manage_window["-FILE_NAME-"].update(" ")
        manage_window["-DEL_SCPT-"].update(disabled = True)
        manage_window["-FILE-"].update(" ")
        manage_window.refresh()
        
        #show files and contents for selection
        if event == "-FILE_LIST-" and len(values["-FILE_LIST-"]) > 0:
            #display a list of installed txt/run files in the folder (if not empty)
            App_Functions.get_file_contents(sg.user_settings_get_entry("-setcamppath-"), values["-FILE_LIST-"])
            #display the name of the file on top of the multiline
            manage_window["-FILE_NAME-"].update(os.path.join(App_Functions.get_folder(sg.user_settings_get_entry("-setcamppath-")), App_Functions.get_file_selection(values["-FILE_LIST-"])))
            #display multiline with content from selected text file
            manage_window["-FILE_TEXT-"].update(App_Functions.get_file_contents(sg.user_settings_get_entry("-setcamppath-"), values["-FILE_LIST-"]))
            selected_folder = App_Functions.get_folder(sg.user_settings_get_entry("-setcamppath-"))
            selected_file = App_Functions.get_file_selection(values["-FILE_LIST-"])
            manage_window["-FILE-"].update(selected_file)
            manage_window["-DEL_SCPT-"].update(disabled = False)
            print(">> MYWIN/CONV list - folder:", selected_folder)
            print(">> MYWIN/CONV list - file:", selected_file)

        #Edit selected file            
        if event in ("-EDIT_SCPT-"):
            if selected_file == []:
                sg.popup(f"Please, select a file!" , font = "Arial, 14", text_color = ("Dark Red"), no_titlebar = True, modal = True, keep_on_top=True)
            else:
                if sg.popup_yes_no(f"Once deleted, {selected_file} can't be restored! Continue?", 
                                    no_titlebar = True, 
                                    modal = True, 
                                    keep_on_top = True) == "Yes":
                    os.remove(os.path.join(selected_folder, selected_file))
                    for i in range(300):
                        sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, message = "    Deleting file...   ", time_between_frames=100)
                    sg.popup_animated(None)
                    manage_window["-FILE_LIST-"].update(App_Functions.extension_to_be_displayed(sg.user_settings_get_entry("-setcamppath-"), values["-TXT-"], values ["-RUN-"], values["-ALL-"]))
                    manage_window["-FILE_NAME-"].update(" ")
                    manage_window["-FILE_TEXT-"].update(" ")
                    manage_window["-DEL_SCPT-"].update(disabled = True)

        #delete selected file            
        if event in ("-DEL_SCPT-"):
            if selected_file == []:
                sg.popup(f"Please, select a file to be deleted!" , font = "Arial, 14", text_color = ("Dark Red"), no_titlebar = True, modal = True, keep_on_top=True)
            else:
                if sg.popup_yes_no(f"Once deleted, {selected_file} can't be restored! Continue?", 
                                    no_titlebar = True, 
                                    modal = True, 
                                    keep_on_top = True) == "Yes":
                    os.remove(os.path.join(selected_folder, selected_file))
                    for i in range(300):
                        sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, message = "    Deleting file...   ", time_between_frames=100)
                    sg.popup_animated(None)
                    manage_window["-FILE_LIST-"].update(App_Functions.extension_to_be_displayed(sg.user_settings_get_entry("-setcamppath-"), values["-TXT-"], values ["-RUN-"], values["-ALL-"]))
                    manage_window["-FILE_NAME-"].update(" ")
                    manage_window["-FILE_TEXT-"].update(" ")
                    manage_window["-DEL_SCPT-"].update(disabled = True)
                    
    manage_window.close()
    return manage_window

