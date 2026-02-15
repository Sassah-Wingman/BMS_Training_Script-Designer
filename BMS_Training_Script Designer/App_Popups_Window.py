from email.policy import default
from re import I
from tkinter import Y
import FreeSimpleGUI as sg
import App_Functions
import App_Images
import App_Workspace_Window

#graph global variables
graph1 = None
graph2 = None
graph3 = None
graph4 = None
graph5 = None
graph6 = None
graph7 = None
graph8 = None
x = 0.0
y = 0.0
counter = 0

# Functions to handle popup windows for adding functions to the training script

# Handle Section function where the variable is the first argument
def section_popup(title, window, list1, list2, list3, list4, summary):
    layout = [[sg.Push(),sg.Input(size = (60, 1), focus = True, font = "_ 12", enable_events = True, key="-ARGSEC-"), sg.Push()],
              [sg.Push(), sg.Button("Add",  size = (15, 2), font = "_ 12", disabled = True, key = "-ADDSEC-"), sg.Button("Cancel",  size = (15, 2), font = "_ 12", key = "-CANCEL_SEC-"), sg.Push()]]
    
    section_popup = sg.Window(title, layout, disable_minimize = True, use_custom_titlebar = True, titlebar_font = "_ 14", grab_anywhere = True, titlebar_icon = App_Images.bms_image, modal=True, finalize=True, size = (700, 180), element_padding = 10, keep_on_top = True)
    
    while True:
        event, values = section_popup.read()
        if event in (sg.WIN_CLOSED, "-CANCEL_SEC-"):
            break
        if event == "-ARGSEC-":
            section_popup["-ADDSEC-"].update(disabled = False)
        if event == "-ADDSEC-":
            section_popup.close()
            App_Functions.Handle_Function(window, list1, list2, list3, list4, values["-ARGSEC-"], summary, " ", values["-ARGSEC-"], None)

    section_popup.close()
    return section_popup

# Handle Input type popups
def input_popup(title, window, list1, list2, list3, list4, script, summary):
    layout = [[sg.Push(), sg.Text(title, font="_ 16"), sg.Push(),],
              [sg.Input(size = (60, 1), focus = True, font = "_ 12", enable_events = True, key = "-ARGTEXT-")],
              [sg.Push(), sg.Button("Add",  size = (15, 2), font = "_ 12", disabled = True, key="-ADDTXT-"), sg.Button("Cancel",  size = (15, 2), font = "_ 12", key="-CANCELTXT-"), sg.Push()]]
    
    text_popup = sg.Window("Text", layout, disable_minimize = True, no_titlebar = True, grab_anywhere = True, modal=True, finalize=True, element_padding = 10, keep_on_top = True)
    
    while True:
        event, values = text_popup.read()
        if event in (sg.WIN_CLOSED, "-CANCELTXT-"):
            break
        if event == "-ARGTEXT-":
            text_popup["-ADDTXT-"].update(disabled = False)
        elif event == "-ADDTXT-":
            text_popup.close()
            App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, values["-ARGTEXT-"], values["-ARGTEXT-"], None)

    text_popup.close()
    return text_popup

# Handle List type popups 
def list_popup(title, window, listcombo1, list1, list2, list3, list4, script, summary, width):
        graph1 = None
        graph2 = None
        graph3 = None
        graph4 = None
        graph5 = None
        graph6 = None
        graph7 = None
        graph8 = None
        listcolor = []
        finallistcolor = []

        layout = [[sg.Push(),sg.Combo(values = listcombo1, size = (width, 1), readonly = True, enable_events = True, key = "-ARGLIST-"), sg.Push()],
                  [sg.Push(), sg.Button("Add", size = (15, 2), font = "_ 12", disabled = True, key="-ADDLIST-"), sg.Button("Cancel", size = (15, 2), font = "_ 12", key="-CANCELLIST-"), sg.Push()]]
    
        list_popup = sg.Window(title, layout, disable_minimize = True, use_custom_titlebar = True, titlebar_font = "_ 14", grab_anywhere = True, titlebar_icon = App_Images.bms_image, modal=True, finalize=True, size = (800, 200), element_padding = 10, keep_on_top = True)
    
        while True:
            event, values = list_popup.read()
            #clear graph images and exit popup
            if event in (sg.WIN_CLOSED, "-CANCELLIST-"):
                App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)
                break

            #handle list selection events and draw sample images on the main graph
            if event == "-ARGLIST-" and script == "SetColor": # and values["-ARGLIST-"] in listcombo1:
                list_popup["-ADDLIST-"].update(disabled = False)
                graph1 = window["-graph-"].draw_text("This is the color you picked!", (-0.75, -0.08), color = values["-ARGLIST-"], font = "arial 8 bold")
                graph2 = window["-graph-"].draw_line((-0.80, -0.80), (-0.60, -0.60), color = values["-ARGLIST-"], width = 1)
                graph3 = window["-graph-"].draw_line((-0.80, -0.70), (-0.60, -0.50), color = values["-ARGLIST-"], width = 2)
                graph4 = window["-graph-"].draw_line((-0.80, -0.60), (-0.60, -0.40), color = values["-ARGLIST-"], width = 3)
                graph5 = window["-graph-"].draw_line((-0.80, -0.50), (-0.60, -0.30), color = values["-ARGLIST-"], width = 4)
                graph6 = window["-graph-"].draw_circle((0.40, 0.60), radius = 0.15, line_color = values["-ARGLIST-"], line_width = 2)
                graph7 = window["-graph-"].draw_circle((0.40, 0.60), radius = 0.10, line_color = values["-ARGLIST-"], line_width = 1)
                graph8 = window["-graph-"].draw_oval((0.50, -0.50), (0.25, -0.25), line_color = values["-ARGLIST-"], line_width = 2)
            elif event == "-ARGLIST-" and script == "SetFontColor":
                list_popup["-ADDLIST-"].update(disabled = False)
                graph1 = window["-graph-"].draw_text("This is the color you picked!", (-0.75, -0.08), color = values["-ARGLIST-"], font = "arial 8 bold")
            elif event == "-ARGLIST-" and script == "SetDrawColor":
                list_popup["-ADDLIST-"].update(disabled = False)
                listcolor.append(App_Functions.Draw_Lines(window, values["-ARGLIST-"]))
                finallistcolor = [item for sublist in listcolor for item in sublist]
                print("Image generated Id's:", listcolor)
                print("Image generated Id's:", finallistcolor)
                # graph2 = window["-graph-"].draw_line((-0.80, -0.80), (-0.60, -0.60), color = values["-ARGLIST-"], width = 1)
                # graph3 = window["-graph-"].draw_line((-0.80, -0.70), (-0.60, -0.50), color = values["-ARGLIST-"], width = 2)
                # graph4 = window["-graph-"].draw_line((-0.80, -0.60), (-0.60, -0.40), color = values["-ARGLIST-"], width = 3)
                # graph5 = window["-graph-"].draw_line((-0.80, -0.50), (-0.60, -0.30), color = values["-ARGLIST-"], width = 4)
                # graph6 = window["-graph-"].draw_circle((0.40, 0.60), radius = 0.15, line_color = values["-ARGLIST-"], line_width = 2)
                # graph7 = window["-graph-"].draw_circle((0.40, 0.60), radius = 0.10, line_color = values["-ARGLIST-"], line_width = 1)
                # graph8 = window["-graph-"].draw_oval((0.50, -0.50), (0.25, -0.25), line_color = values["-ARGLIST-"], line_width = 2)
            elif event == "-ARGLIST-" and script == "SetFontBGColor":
                #listcolor=[]
                list_popup["-ADDLIST-"].update(disabled = False)
                a = 0.15
                b = 0.21
                c = 0.18
                for i in listcombo1:
                    finallistcolor.append(window["-graph-"].draw_rectangle((-0.98, a), (-0.52, b), fill_color = values["-ARGLIST-"], line_color = values["-ARGLIST-"]) )
                    finallistcolor.append(window["-graph-"].draw_text("This is how your text will look like!", (-0.75, c), color = i, font = "arial 8 bold"))
                    # listcolor.append(window["-graph-"].draw_rectangle((-0.98, a), (-0.52, b), fill_color = values["-ARGLIST-"], line_color = values["-ARGLIST-"]) )
                    # listcolor.append(window["-graph-"].draw_text("This is how your text will look like!", (-0.75, c), color = i, font = "arial 8 bold"))
                    # graph1 = window["-graph-"].draw_rectangle((-0.98, a), (-0.52, b), fill_color = values["-ARGLIST-"], line_color = values["-ARGLIST-"]) 
                    # graph2 = window["-graph-"].draw_text("This is how your text will look like!", (-0.75, c), color = i, font = "arial 8 bold")
                    # listcolor.append(graph1)
                    # listcolor.append(graph2)
                    a = a - 0.15
                    b = b - 0.15
                    c = c - 0.15
                print("Image generated Id's:", listcolor)
            #handle flash selection events and draw sample images on the main graph
            elif event == "-ARGLIST-" and script == "SetFlash":
                list_popup["-ADDLIST-"].update(disabled = False)
                graph1 = window["-graph-"].draw_text("flashing effect to be added later.", (-0.75, -0.08), color = "yellow", font = "arial 8 bold")
            elif event == "-ARGLIST-" and script == "SetFontFlash":
                list_popup["-ADDLIST-"].update(disabled = False)
                graph1 = window["-graph-"].draw_text("flashing effect to be added later.", (-0.75, -0.08), color = "yellow", font = "arial 8 bold")
            elif event == "-ARGLIST-" and script == "SetDrawFlash":
                list_popup["-ADDLIST-"].update(disabled = False)
                graph1 = window["-graph-"].draw_text("flashing effect to be added later.", (-0.75, -0.08), color = "yellow", font = "arial 8 bold")
            elif event == "-ARGLIST-" and script == "ClearLast":
                list_popup["-ADDLIST-"].update(disabled = False)
            elif event == "-ARGLIST-" and script == "SetTextBoxed":
                list_popup["-ADDLIST-"].update(disabled = False)
            elif event == "-ARGLIST-" and script == "SetGunAmmo":
                list_popup["-ADDLIST-"].update(disabled = False)
            elif event == "-ARGLIST-" and script == "SetMavCoolTime":
                list_popup["-ADDLIST-"].update(disabled = False)
            elif event == "-ARGLIST-" and script == "Wait":
                list_popup["-ADDLIST-"].update(disabled = False)
            elif event == "-ARGLIST-" and script == "WaitGameTime":
                list_popup["-ADDLIST-"].update(disabled = False)
            elif event == "-ARGLIST-" and script == "WaitSoundStop":
                list_popup["-ADDLIST-"].update(disabled = False)


            #handle add button event to add the selected item to the script
            if event == "-ADDLIST-":
                try:
                    for i in finallistcolor:
                        print("Image generated Id's finallistcolor:", finallistcolor)
                        print(i)
                        window["-graph-"].delete_figure(i)  # Clear the previous figures
                except:
                    pass
                App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)   #must be the first call to do before closing the popup
                if script == "SetColor" or script == "SetFontColor" or script == "SetDrawColor" or script == "SetFontBGColor":   
                    item_selected = App_Functions.get_color_hex(listcombo1.index(values["-ARGLIST-"]))
                elif script == "SetFlash" or script == "SetFontFlash" or script == "SetDrawFlash":
                    item_selected = App_Functions.get_flash_hex(listcombo1.index(values["-ARGLIST-"]))
                elif script == "ClearLast":
                    if values["-ARGLIST-"] == "0":
                        item_selected = None
                        summary = "Only last drawn element will be erased."
                    else:
                        item_selected = values["-ARGLIST-"]
                elif script == "SetTextBoxed":
                    item_selected = App_Functions.get_BG_integer(listcombo1.index(values["-ARGLIST-"]))
                elif script == "SetGunAmmo":
                        item_selected = values["-ARGLIST-"]
                elif script == "SetMavCoolTime":
                        item_selected = values["-ARGLIST-"]
                elif script == "Wait":
                        item_selected = values["-ARGLIST-"]
                elif script == "WaitGameTime":
                        item_selected = values["-ARGLIST-"]
                elif script == "WaitSoundStop":
                        item_selected = values["-ARGLIST-"]

                list_popup.close()
                App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, item_selected, values["-ARGLIST-"], None)

        list_popup.close()
        return list_popup

# Handle List + Input popups 
def list_input_popup(title, window, listcombo1, list1, list2, list3, list4, script, summary, width):
    graph1 = None

    layout = [[sg.Push(),sg.Combo(values = listcombo1, size = (width, 1), readonly = True, enable_events = True, key = "-ARGLISTINP-"), sg.Push()],
                [sg.Push(),sg.Input(size = (60, 1), disabled_readonly_background_color = "Dark gray", disabled = True, focus = True, font = "_ 12", enable_events = True, key = "-ARGINPT-"),sg.Push()],
                [sg.Push(), sg.Button("Add", size = (15, 2), font = "_ 12", disabled = True, key="-ADDLISTINP-"), sg.Button("Cancel", size = (15, 2), font = "_ 12", key="-CANCELLISTINP-"), sg.Push()]]
    
    list_input_popup = sg.Window(title, layout, disable_minimize = True, use_custom_titlebar = True, titlebar_font = "_ 14", grab_anywhere = True, titlebar_icon = App_Images.bms_image, modal=True, finalize=True, size = (800, 200), element_padding = 10, keep_on_top = True)
    

    while True:
        event, values = list_input_popup.read()
        if event in (sg.WIN_CLOSED, "-CANCELLISTINP-"):
            App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)
            break

        #handle list selection events and draw sample images on the main graph
        if event == "-ARGLISTINP-":
            list_input_popup["-ARGINPT-"].update(disabled = False)
        if event == "-ARGINPT-":
            window["-graph-"].delete_figure(graph1)
            graph1 = window["-graph-"].draw_text(text = values["-ARGINPT-"], location = (-0.80, -0.04), color = "Red", font = "arial 8 bold")
            list_input_popup["-ADDLISTINP-"].update(disabled = False)

        
        #handle add button event to add the selected item to the script
        if event == "-ADDLISTINP-":
            App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)   #must be the first call to do before closing the popup
            App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, values["-ARGLISTINP-"], values["-ARGINPT-"], None)
            list_input_popup.close()

    list_input_popup.close()
    return list_input_popup

# Handle List + List popups
def list_list_popup(title, window, listcombo1, listcombo2, list1, list2, list3, list4, script, summary, width1, width2):
    graph1 = None
    graph2 = None
    graph3 = None
    graph4 = None
    global x 
    global y 
    global counter
    # X = 0.0
    # Y = 0.0

    layout = [[sg.Push(),sg.Text(text = "Horizontal Axis (x)", font = "_ 12", text_color = "white"),
               sg.Push(),sg.Text(text = "Vertical Axis (y)", font = "_ 12", text_color = "white"), sg.Push()],
              [sg.Push(),sg.Combo(values = listcombo1, size = (width1, 1), readonly = True, enable_events = True, key = "-ARGLIST1-"),
               sg.Push(),sg.Combo(values = listcombo2, size = (width2, 1), readonly = True, disabled = True, enable_events = True, key = "-ARGLIST2-"), sg.Push()],
              [sg.Push(), sg.Button("Add", size = (15, 2), font = "_ 12", disabled = True, key="-ADDCOORD-"), sg.Button("Cancel", size = (15, 2), font = "_ 12", key="-CANCELCOORD-"), sg.Push()]]
    
    list_list_popup = sg.Window(title, layout, disable_minimize = True, use_custom_titlebar = True, titlebar_font = "_ 14", grab_anywhere = True, titlebar_icon = App_Images.bms_image, modal=True, finalize=True, size = (800, 200), element_padding = 10, keep_on_top = True)
    

    while True:
        event, values = list_list_popup.read()
        print("Event: ", event, "Values: ", values)
        if event in (sg.WIN_CLOSED, "-CANCELCOORD-"):
            App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)
            break

        #handle list selection events and draw sample images on the main graph
        #enable second list when first is selected
        if event == "-ARGLIST1-" and script == "SetCursor" or script == "MoveCursor" or script == "SetPanTilt" or script == "MovePanTilt":
            print("List of Coordinates/Degrees:", listcombo1)
            list_list_popup["-ARGLIST2-"].update(disabled = False)
        #draw cursor position on graph
        elif event == "-ARGLIST2-" and values["-ARGLIST1-"] and script == "SetCursor":
            print ("X:", values["-ARGLIST1-"], "Y:", values["-ARGLIST2-"])
            window["-graph-"].delete_figure(graph1)
            window["-graph-"].delete_figure(graph2)
            tempx = float(values["-ARGLIST1-"])
            tempy = float(values["-ARGLIST2-"])
            graph1 = window["-graph-"].draw_text(text = "O", location = (tempx, tempy), color = "white", font = "arial 10 bold")
            graph2 = window["-graph-"].draw_text(text = "+", location = (tempx, tempy), color = "Magenta", font = "arial 16")
            list_list_popup["-ADDCOORD-"].update(disabled = False)
        elif event == "-ARGLIST1-" and values["-ARGLIST2-"] and script == "SetCursor":
            print ("X:", values["-ARGLIST1-"], "Y:", values["-ARGLIST2-"])
            window["-graph-"].delete_figure(graph1)
            window["-graph-"].delete_figure(graph2)
            tempx = float(values["-ARGLIST1-"])
            tempy = float(values["-ARGLIST2-"])
            graph1 = window["-graph-"].draw_text(text = "O", location = (tempx, tempy), color = "white", font = "arial 10 bold")
            graph2 = window["-graph-"].draw_text(text = "+", location = (tempx, tempy), color = "Magenta", font = "arial 16")
        #draw move cursor position on graph            
        
        if event == "-ARGLIST2-" and values["-ARGLIST1-"] and script == "MoveCursor":
            window["-graph-"].delete_figure(graph1)
            window["-graph-"].delete_figure(graph2)
            window["-graph-"].delete_figure(graph3)
            window["-graph-"].delete_figure(graph4)
            graph1 = window["-graph-"].draw_text(text = "O", location = (x, y), color = "Yellow", font = "arial 10 bold")
            graph2 = window["-graph-"].draw_text(text = "+", location = (x, y), color = "Magenta", font = "arial 16")
            X = round(x + float(values["-ARGLIST1-"]), 2)
            Y = round(y + float(values["-ARGLIST2-"]), 2)
            graph4 = window["-graph-"].draw_text(text = "O", location = (X, Y), color = "Magenta", font = "arial 16")
            graph3 = window["-graph-"].draw_text(text = "+", location = (X, Y), color = "green1", font = "arial 16 bold")
            list_list_popup["-ADDCOORD-"].update(disabled = False)
        elif event == "-ARGLIST1-" and values["-ARGLIST2-"] and script == "MoveCursor":
            window["-graph-"].delete_figure(graph1)
            window["-graph-"].delete_figure(graph2)
            window["-graph-"].delete_figure(graph3)
            window["-graph-"].delete_figure(graph4)
            graph1 = window["-graph-"].draw_text(text = "O", location = (x, y), color = "Yellow", font = "arial 10 bold")
            graph2 = window["-graph-"].draw_text(text = "+", location = (x, y), color = "Magenta", font = "arial 16")
            X = round(x + float(values["-ARGLIST1-"]), 2)
            Y = round(y + float(values["-ARGLIST2-"]), 2)
            graph4 = window["-graph-"].draw_text(text = "O", location = (X, Y), color = "Magenta", font = "arial 16")
            graph3 = window["-graph-"].draw_text(text = "+", location = (X, Y), color = "green1", font = "arial 16 bold")
            list_list_popup["-ADDCOORD-"].update(disabled = False)
     
        #handle pan/tilt selection events and draw sample images on the main graph (TBD)
        if event == "-ARGLIST2-" and values["-ARGLIST1-"] and script == "SetPanTilt":
            print ("Radian X:", values["-ARGLIST1-"], "Radian Y:", values["-ARGLIST2-"])
            x = App_Functions.get_radians(listcombo1.index(values["-ARGLIST1-"]))
            y = App_Functions.get_radians(listcombo2.index(values["-ARGLIST2-"]))
            #list_list_popup["-ADDCOORD-"].update(disabled = False)
        elif event == "-ARGLIST2-" and values["-ARGLIST1-"] and script == "MovePanTilt":
            print ("Radian X:", values["-ARGLIST1-"], "Radian Y:", values["-ARGLIST2-"])
            deltax = float(App_Functions.get_radians(listcombo1.index(values["-ARGLIST1-"])))
            deltay = float(App_Functions.get_radians(listcombo2.index(values["-ARGLIST2-"])))
            X = round(deltax + tempx, 2)
            Y = round(deltay + tempy, 2)
        list_list_popup["-ADDCOORD-"].update(disabled = False)
        #handle add button event to add the selected item to the script
        if event == "-ADDCOORD-":
            if script == "SetCursor":
                item_selected1 = values["-ARGLIST1-"]
                item_selected2 = values["-ARGLIST2-"]
                x = float(values["-ARGLIST1-"])
                y = float(values["-ARGLIST2-"])
                window["-cposx-"].update(x)
                window["-cposy-"].update(y)
                window["-graph-"].draw_text(text = "O", location = (x, y), color = "Red", font = "arial 10 bold")
                window["-graph-"].draw_text(text = "+", location = (x, y), color = "Cyan", font = "arial 16")
                window["-graph-"].draw_text(text = counter, location = (x+0.03, y+0.03), color = "Cyan", font = "arial 12")
                counter = counter + 1
            elif script == "MoveCursor":
                item_selected1 = values["-ARGLIST1-"]
                item_selected2 = values["-ARGLIST2-"]
                window["-cposx-"].update(X)
                window["-cposy-"].update(Y)
                x=X
                y=Y
                if X < -1.0 or X > 1.0 or Y < -1.0 or Y > 1.0:
                    sg.popup_ok("The new cursor position is out of bounds!", font = "_ 12", title="Warning!", keep_on_top=True)
                window["-graph-"].draw_text(text = "O", location = (x, y), color = "Red", font = "arial 10 bold")
                window["-graph-"].draw_text(text = "+", location = (x, y), color = "Cyan", font = "arial 16")
                window["-graph-"].draw_text(text = counter, location = (x+0.03, y+0.03), color = "Cyan", font = "arial 12")
                counter = counter + 1
            elif script == "SetPanTilt": 
                item_selected1 = App_Functions.get_radians(listcombo1.index(values["-ARGLIST1-"]))
                item_selected2 = App_Functions.get_radians(listcombo2.index(values["-ARGLIST2-"]))
            elif script == "MovePanTilt":  
                item_selected1 = App_Functions.get_radians(listcombo1.index(values["-ARGLIST1-"]))
                item_selected2 = App_Functions.get_radians(listcombo2.index(values["-ARGLIST2-"]))
                if X < -6.2832 or X > 6.2832 or Y < -6.2832 or Y > 6.2832:
                    sg.popup_ok("The new pan til position is out of bounds!", font = "_ 12", title="Warning!", keep_on_top=True)

            App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)   #must be the first call to do before closing the popup
            App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, item_selected1, item_selected2, None)
            list_list_popup.close()

    list_list_popup.close()
    return list_list_popup

def list_list_list_popup(title, window, listcombo1, listcombo2, list1, list2, list3, list4, script, summary, width1):
    graph1 = None
    graph2 = None
    graph3 = None
    graph4 = None
    global x 
    global y 
 

    layout = [[sg.Push(), sg.Text(text = "Set the cursor coordinate first!", font = "_ 16", text_color = "Red"), sg.Push()],
              [sg.Push(), sg.Text(text = "Last coordinate (X,Y):", font = "_ 12", text_color = "white"),
               sg.Text(x, font = "_ 12", text_color = "Yellow"),
               sg.Text(y, font = "_ 12", text_color = "Yellow"), sg.Push()],
              [sg.Push(), sg.Text(text = "Time in seconds", font = "_ 12", text_color = "white"), sg.Push()],
              [sg.Push(), sg.Combo(values = listcombo1, size = (width1, 1), readonly = True, enable_events = True, key = "-ARGTIME-"), sg.Push()],
              [sg.Push(), sg.Text(text = " ", font = "_ 12", text_color = "white", key = "-TXT1-"), sg.Push()],
              [sg.Push(), sg.Text(text = " ", font = "_ 12", text_color = "white", key = "-TXT2-"), sg.Push(),
               sg.Push(), sg.Text(text = " ", font = "_ 12", text_color = "white", key = "-TXT3-"), sg.Push()],
              [sg.Push(), sg.Combo(values = listcombo2, size = (width1, 1), readonly = True, disabled = True, enable_events = True, key = "-ARGX1-"), sg.Push(), 
               sg.Push(), sg.Combo(values = listcombo2, size = (width1, 1), readonly = True, disabled = True, enable_events = True, key = "-ARGY1-"), sg.Push()],
              [sg.Push(), sg.Text(text = " ", font = "_ 12", text_color = "white", key = "-TXT4-"), sg.Push()],
              [sg.Push(), sg.Combo(values = listcombo2, size = (width1, 1), readonly = True, disabled = True, visible = True, enable_events = True, key = "-ARGX2-"), sg.Push(),
               sg.Push(), sg.Combo(values = listcombo2, size = (width1, 1), readonly = True, disabled = True, visible = True, enable_events = True, key = "-ARGY2-"), sg.Push()],
              [sg.Push(), sg.Button("Add", size = (15, 2), font = "_ 12", disabled = True, key="-ADDMULT-"), sg.Button("Cancel", size = (15, 2), font = "_ 12", key="-CANCELMULT-"), sg.Push()]]
    
    list_list_list_popup = sg.Window(title, layout, disable_minimize = True, use_custom_titlebar = True, titlebar_font = "_ 14", grab_anywhere = True, titlebar_icon = App_Images.bms_image, modal=True, finalize=True, size = (800, 500), element_padding = 10, keep_on_top = True)
    

    while True:
        event, values = list_list_list_popup.read()
        print("Event: ", event, "Values: ", values)
        if event in (sg.WIN_CLOSED, "-CANCELMULT-"):
            App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)
            break

        # configure the popup window based on the script selected 
        if event == "-ARGTIME-" and script == "Oval":
            print("Graph drawn with Radius1:", x, "Radius2:", y)
            list_list_list_popup["-ARGX1-"].update(disabled = False)
            list_list_list_popup["-ARGY1-"].update(disabled = False)
            list_list_list_popup["-ARGX2-"].update(visible = False)
            list_list_list_popup["-ARGY2-"].update(visible = False)
            list_list_list_popup["-TXT2-"].update("Set the radius value for a circle")
            list_list_list_popup["-TXT3-"].update("Set the secundary value for an oval")
        elif event == "-ARGTIME-" and script == "Line":
            print("List of Coordinates/Degrees:", listcombo1)
            list_list_list_popup["-ARGX1-"].update(disabled = False)
            list_list_list_popup["-ARGY1-"].update(visible = True)
            list_list_list_popup["-ARGX2-"].update(visible = True)
            list_list_list_popup["-ARGY2-"].update(visible = True)
            list_list_list_popup["-TXT2-"].update("Set the coordinates X and Y where the line starts")
            list_list_list_popup["-TXT4-"].update("Set the coordinates X and Y where the line ends")
        elif event == "-ARGTIME-" and script == "WaitMouse":
            print("List of Coordinates/Degrees:", listcombo1)
            list_list_list_popup["-ARGX1-"].update(disabled = False)
            list_list_list_popup["-TXT2-"].update("Set the coordinates X and Y where the mouse should hover")
            list_list_list_popup["-TXT4-"].update("Set the distance from this coordinate to enable mouse hover")
            list_list_list_popup["-ARGY2-"].update(visible = True)
        
        #draw the circle and oval on graph
        if event == "-ARGX1-" and not values["-ARGY1-"] and script == "Oval":
            print("Graph Circle with Radius1:", values["-ARGX1-"])
            window["-graph-"].delete_figure(graph1)
            graph1 = window["-graph-"].draw_circle(center_location = (x, y), radius = float(values["-ARGX1-"]), line_color = "Red", line_width = 1)
            list_list_list_popup["-ADDMULT-"].update(disabled = False)
        elif event == "-ARGY1-" and values["-ARGX1-"] and script == "Oval":
            print("Graph Oval with Radius1:", values["-ARGX1-"], "Radius2:", values["-ARGY1-"])
            window["-graph-"].delete_figure(graph1)
            TOPLEFTX = (x - (float(values["-ARGX1-"])))
            TOPLEFTY = (y + 3*float(values["-ARGY1-"]))
            BOTTOMRIGHTX = (x + (float(values["-ARGX1-"])))
            BOTTOMRIGHTY = (y - 3*float(values["-ARGY1-"]))
            print("Top Left:", TOPLEFTX, TOPLEFTY, "Bottom Right:", BOTTOMRIGHTX, BOTTOMRIGHTY)
            graph1 = window["-graph-"].draw_oval(top_left = (TOPLEFTX, TOPLEFTY), bottom_right = (BOTTOMRIGHTX, BOTTOMRIGHTY), line_color = "Red", line_width = 1)
            list_list_list_popup["-ADDMULT-"].update(disabled = False)
        elif event == "-ARGX1-" and values["-ARGY1-"] and script == "Oval":
            print("Graph Oval with Radius1:", values["-ARGX1-"], "Radius2:", values["-ARGY1-"])
            window["-graph-"].delete_figure(graph1)
            TOPLEFTX = (x - (float(values["-ARGX1-"])))
            TOPLEFTY = (y + 2*float(values["-ARGY1-"]))
            BOTTOMRIGHTX = (x + (float(values["-ARGX1-"])))
            BOTTOMRIGHTY = (y - 2*float(values["-ARGY1-"]))
            print("Top Left:", TOPLEFTX, TOPLEFTY, "Bottom Right:", BOTTOMRIGHTX, BOTTOMRIGHTY)
            graph1 = window["-graph-"].draw_oval(top_left = (TOPLEFTX, TOPLEFTY), bottom_right = (BOTTOMRIGHTX, BOTTOMRIGHTY), line_color = "Red", line_width = 1)
            list_list_list_popup["-ADDMULT-"].update(disabled = False)

        #Draw the line on graph
        
        



        if event == "-ADDMULT-":
            if script == "Oval":
                item_selected1 = values["-ARGTIME-"]
                item_selected2 = values["-ARGX1-"]
                item_selected3 = values["-ARGY1-"]
            elif script == "Line":
                item_selected1 = values["-ARGLIST1-"]
                item_selected2 = values["-ARGLIST2-"]
                window["-cposx-"].update(X)
                window["-cposy-"].update(Y)
                if X < -1.0 or X > 1.0 or Y < -1.0 or Y > 1.0:
                    sg.popup_ok("The new cursor position is out of bounds!", font = "_ 12", title="Warning!", keep_on_top=True)
            elif script == "WaitMouse": 
                item_selected1 = App_Functions.get_radians(listcombo1.index(values["-ARGLIST1-"]))
                item_selected2 = App_Functions.get_radians(listcombo2.index(values["-ARGLIST2-"]))
         

            App_Functions.clear_image(window, graph1, graph2, graph3, graph4, graph5, graph6, graph7, graph8)   #must be the first call to do before closing the popup
            App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, item_selected1, item_selected2, item_selected3)
            list_list_list_popup.close()

    list_list_list_popup.close()
    return list_list_list_popup


# Handle Spin type popups
def spin_popup(title, window, list1, list2, list3, list4, script, summary):
    layout = [[sg.Push(), sg.Text(title, font="_ 16"), sg.Push(),],
              [sg.Input(size = (60, 1), visible = False, focus = True, font="_ 12", enable_events = True, key = "-ARGTEXT-")],
              [sg.Spin(size = (3, 1), visible = True, focus = True, font="_ 12", wrap = True, enable_events = True, key = "-ARGNUM1-"),
               sg.Spin(size = (3, 1), visible = True, focus = True, font="_ 12", wrap = True, enable_events = True, key = "-ARGNUM2-"),
               sg.Spin(size = (3, 1), visible = True, focus = True, font="_ 12", wrap = True, enable_events = True, key = "-ARGNUM3-"),
               sg.Spin(size = (3, 1), visible = False, focus = True, font="_ 12", wrap = True, enable_events = True, key = "-ARGNUM4-"),
               sg.Spin(size = (3, 1), visible = False, focus = True, font="_ 12", wrap = True, enable_events = True, key = "-ARGNUM5-"),
               sg.Spin(size = (3, 1), visible = False, focus = True, font="_ 12", wrap = True, enable_events = True, key = "-ARGNUM6-")],
              [sg.Push(), sg.Button("Add",  size = (15, 2), font = "_ 12", disabled = True, key="-ADDNUM-"), sg.Button("Cancel",  size = (15, 2), font = "_ 12", key="-CANCELNUM-"), sg.Push()]]
    
    text_popup = sg.Window("Text", layout, disable_minimize = True, no_titlebar = True, grab_anywhere = True, modal=True, finalize=True, element_padding = 10, keep_on_top = True)
    
    while True:
        event, values = text_popup.read()
        if event in (sg.WIN_CLOSED, "-CANCELNUM-"):
            break
        if event == "-ARGNUM1-":
            text_popup["-ADDNUM1-"].update(disabled = False)
        elif event == "-ADDNUM-":
            text_popup.close()
            App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, values["-ARGNUM1-"], values["-ARGNUM1-"], None)

    text_popup.close()
    return text_popup

# Handle Fuel function due to its special approach
def fuel_window(window, listfwd, listaft, listrsv, listwig, listexw, listexc, list1, list2, list3, list4, script, summary):
        
    listfuel = []    
  
    internal_fwd = sg.Push(), sg.Frame("Internal FWD Tanks", 
                    [[sg.Push(), sg.Text(text = "Internal FWD (Max 2.770 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push()],
                     [sg.Push(), sg.Combo(values = listfwd, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGFWD-"), sg.Push()],
                     [sg.Push(), sg.Text(text = "Internal FWD Reservoir (Max 480 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push()],
                     [sg.Push(), sg.Combo(values = listrsv, size = (10, 1), readonly = True, enable_events = True, key = "-ARGFWDR-"), sg.Push()]],
            title_color = "#64778d", font = "_ 12 bold", size = (300,180), title_location = sg.TITLE_LOCATION_TOP, vertical_alignment = "top"), sg.Push() 
                  
    wing_tanks = sg.Push(), sg.Frame("Wing Tanks",
                [[sg.Text(text = "Internal LEFT Wing (Max 550 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push(),
                  sg.Push(), sg.Text(text = "Internal RIGHT Wing (Max 550 lbs)", font = "_ 10", text_color = "#ffffff")],
                 [sg.Combo(values = listwig, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGWINLH-"), sg.Push(),
                  sg.Push(), sg.Combo(values = listwig, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGWINRH-")]],
            title_color = "#64778d", font = "_ 12 bold", size = (600,100), title_location = sg.TITLE_LOCATION_TOP, vertical_alignment = "top"), sg.Push() 
                   
    internal_aft = sg.Push(), sg.Frame("Internal AFT Tanks",                   
                [[sg.Push(), sg.Text(text = "Internal AFT Reservoir (Max 480 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push()],
                [sg.Push(), sg.Combo(values = listrsv, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGAFTR-"), sg.Push()],
                [sg.Push(), sg.Text(text = "Internal AFT (Max 2330 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push()],
                [sg.Push(), sg.Combo(values = listaft, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGAFT-"), sg.Push()]],
            title_color = "#64778d", font = "_ 12 bold", size = (300,180), title_location = sg.TITLE_LOCATION_TOP, vertical_alignment = "top"), sg.Push() 

    external_tanks = sg.Push(), sg.Frame("External Tanks",                   
                    [[sg.Text(text = "External LEFT Wing (Max 2516 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push(),
                    sg.Push(), sg.Text(text = "External Centerline (Max 2040 lbs)", font = "_ 10", text_color = "#ffffff",), sg.Push(),
                    sg.Push(), sg.Text(text = "External RIGHT Wing (Max 2516 lbs)", font = "_ 10", text_color = "#ffffff")],
                    [sg.Combo(values = listexw,  size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGEXLH-"), sg.Push(),
                    sg.Push(), sg.Combo(values = listexc, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGEXCT-"), sg.Push(),
                    sg.Push(), sg.Combo(values = listexw, size = (10, 1), disabled = True, readonly = True, enable_events = True, key = "-ARGEXRH-")]],
            title_color = "#64778d", font = "_ 12 bold", size = (700,100), title_location = sg.TITLE_LOCATION_TOP, vertical_alignment = "top"), sg.Push() 
                   
    total_fuel = sg.Push(), [sg.Text("Total Fuel Selected (Max 14.234 lbs): ", font = "_ 12 bold", text_color = "#ffffff"),
                            sg.Text("0 lbs", font = "_ 12 bold", text_color = "#000000", key = "-TOTALFUEL-"), sg.Push()],
        
    buttons_fuel = sg.Push(), [[sg.Push(), sg.Text("Note: There are no sanity checks if you have entered the correct fuel distribution.", font = "_ 12 bold", text_color = "dark red"), sg.Push(),],
                                [sg.Push(), sg.Button("Add", size = (15, 2), font = "_ 12", disabled = True, key="-ADDFUEL-"), sg.Button("Cancel", size = (15, 2), font = "_ 12", key="-CANCELFUEL-"), sg.Push(),]]
    
    layout = [[internal_fwd], [wing_tanks], [internal_aft], [external_tanks], [total_fuel], [buttons_fuel]] 
        
    fuel_window = sg.Window("Refuel your F16 tanks.", layout, disable_minimize = True, use_custom_titlebar = True, titlebar_font = "_ 14", grab_anywhere = True, titlebar_icon = App_Images.bms_image, modal=True, finalize=True, size = (800,850), element_padding = 10, keep_on_top = True)
  
    while True:
        event, values = fuel_window.read()

        #exit popup
        if event in (sg.WIN_CLOSED, "-CANCELFUEL-"):
            break

        #handle fuel selection events and enable the next combobox
        if event == "-ARGFWDR-":
            fuel_window["-ARGAFTR-"].update(disabled = False)
        if event == "-ARGAFTR-":
            fuel_window["-ARGFWD-"].update(disabled = False)
        if event == "-ARGFWD-":  
            fuel_window["-ARGAFT-"].update(disabled = False)
        if event == "-ARGAFT-":
            fuel_window["-ARGWINLH-"].update(disabled = False)
        if event == "-ARGWINLH-":
            fuel_window["-ARGWINRH-"].update(disabled = False)
        if event == "-ARGWINRH-":
            fuel_window["-ARGEXLH-"].update(disabled = False)
        if event == "-ARGEXLH-":
            fuel_window["-ARGEXRH-"].update(disabled = False)
        if event == "-ARGEXRH-":
            fuel_window["-ARGEXCT-"].update(disabled = False)
        if event == "-ARGEXCT-":
            fuel_window["-ADDFUEL-"].update(disabled = False)

        #update the total fuel value when all comboboxes are selected
        try:
            fuel_window["-TOTALFUEL-"].update(int(values["-ARGFWDR-"]) + 
                                                int(values["-ARGAFTR-"]) + 
                                                int(values["-ARGFWD-"]) +
                                                int(values["-ARGAFT-"]) +
                                                int(values["-ARGWINLH-"]) +
                                                int(values["-ARGWINRH-"]) +
                                                int(values["-ARGEXLH-"]) +
                                                int(values["-ARGEXRH-"]) +
                                                int(values["-ARGEXCT-"]))
        except:
            pass

        #handle add button event to adjust the list to the fuel distribuition standart
        if event == "-ADDFUEL-":
            listfuel.append(values["-ARGFWDR-"])
            listfuel.append(values["-ARGAFTR-"])
            listfuel.append(values["-ARGFWD-"])
            listfuel.append("0")
            listfuel.append(values["-ARGAFT-"])
            listfuel.append(values["-ARGWINRH-"])
            listfuel.append(values["-ARGWINLH-"])
            listfuel.append("0")
            listfuel.append(values["-ARGEXRH-"])
            listfuel.append("0")
            listfuel.append("0")
            listfuel.append(values["-ARGEXLH-"])
            listfuel.append("0")
            listfuel.append(values["-ARGEXCT-"])
            print("Fuel list to be added to the script: ", listfuel)
            item_selected = listfuel
            #calculate total fuel for summary
            totalfuel = int(values["-ARGFWDR-"]) + int(values["-ARGAFTR-"]) + int(values["-ARGFWD-"]) + int(values["-ARGAFT-"]) + int(values["-ARGWINLH-"]) + int(values["-ARGWINRH-"]) + int(values["-ARGEXLH-"]) + int(values["-ARGEXRH-"]) + int(values["-ARGEXCT-"])
            totalfuelstr = str(totalfuel)
            print("Total fuel to be added to the script: ", totalfuelstr)
            #pass information back to main window
            App_Functions.Handle_Function(window, list1, list2, list3, list4, script, summary, item_selected, totalfuelstr, None)
            fuel_window.close()

    fuel_window.close()
    return fuel_window
