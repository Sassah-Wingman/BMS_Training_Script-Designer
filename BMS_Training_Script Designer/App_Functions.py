from operator import index

import FreeSimpleGUI as sg
from math import radians
import os
from pathlib import Path
import winreg


ListOfColorsHex = ["0xFFFF0000", "0x00FFFF00", "0x0000FFFF", "0x00FF00FF", "0xFF00FF00", "0xFFFFFFFF", "0x00000000"]
ListOfFlashHex = ["0x100", "0x200", "0x300", "0x400", "0x500", "0x600", "0x700", "0x800", "0x900", "0"]
ListOfWidthFloat = [0.002, 0.005, 0.008, 0.01, 0.015, 0.02, 0.05, 0.1, 0.2, 0.3, 0.5, 0.100]
ListOfFontInt = ["0", "1", "2"]
ListOfSwitchInt = ["0", "2"]
ListOfRadians = []
coord_list = []

#create a list of all installed BMS
def get_list_of_bms_path():
     list_of_bms_path = []
     for path_ in get_list_of_installed_bms_path().values():
         list_of_bms_path.append(path_)
         print("=>functions - list of bms: ", list_of_bms_path)
     return list_of_bms_path

#Find all BMS installed using winreg
def get_list_of_installed_bms_path():
    BMS_sub_key = "SOFTWARE\WOW6432Node\Benchmark Sims"
    BMS_Sub_key_name = "baseDir"
    list_of_bms_path_keys = []
    list_of_bms_path_address = []
    try:
        hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, BMS_sub_key, 0, winreg.KEY_READ)
        index = 0
        while True:
            try:
                key_name = winreg.EnumKey(hkey, index)
                hsubkey = winreg.OpenKey(hkey, key_name)
                sub_key_value = winreg.QueryValueEx(hsubkey, BMS_Sub_key_name)[0]
                print("=>functions/path: ", f"{key_name} : {sub_key_value}")
                list_of_bms_path_keys.append(key_name)
                list_of_bms_path_address.append(sub_key_value)
                sim_path = sub_key_value + "\Data\Sim"
                print("=>functions/path: - Sim path: ", sim_path)
                for entry in os.listdir(sim_path):
                    if os.path.isdir(os.path.join(sim_path, entry)):
                        print("=>functions/path: - Sim folder: ", entry)
                winreg.CloseKey(hsubkey)
                index += 1
            except OSError:
                break
    except FileNotFoundError:
        print("=>functions/path: - >>>Falcon BMS not found!<<<")
        sg.popup_ok("Ops! Falcon BMS sees to be not installed in this computer!", text_color = ("red"), no_titlebar = True, keep_on_top = True, modal = True)
    finally:
        if hkey:
            winreg.CloseKey(hkey)
    list_of_installed_bms = dict(zip(list_of_bms_path_keys, list_of_bms_path_address))
    print("=>functions/path: ", list_of_installed_bms)
    print("=>functions/path: - regKeys: ", list_of_installed_bms.keys())
    print("=>functions/path: - regValues: ", list_of_installed_bms.values())
    return list_of_installed_bms

#convert folder name from list to string
def get_folder (_folder):
    folder_address = _folder
    print("=> MYFUN/FOLD - fold selected: ", folder_address)
    return folder_address   

#get file selected and convert it from list to string
def get_file_selection (_filelist):
    print("=> MYFUN/FILE - in: ", _filelist)
    file_selection = _filelist [0]
    print("=> MYFUN/FILE - out: ", file_selection)
    return file_selection

#get content inside the file
def get_file_contents (_folder, _filelist):
    with open(os.path.join(get_folder(_folder), get_file_selection(_filelist))) as file_to_read:
        contents_in_file=file_to_read.read()
        #print(">>>> MYFUN/CONT - file contents: ", contents_in_file)
    return contents_in_file

def get_flatten_list(_list):
    flat_list = []
    for l in _list:
        flat_list.extend(l)
    return flat_list

def messages(window):
    window["-DESC-"].update("test")

def clear_fields(window):
    #reset argument fields
    window["-ARGCOMMENT-"].update(disabled = True)
    window["-ARGLINETM-"].update(disabled = True)
    window["-ARGLINEX1-"].update(disabled = True)
    window["-ARGLINEY1-"].update(disabled = True)
    window["-ARGLINEX2-"].update(disabled = True)
    window["-ARGLINEY2-"].update(disabled = True)
    window["-ARGOVALTM-"].update(disabled = True)
    window["-ARGOVALX-"].update(disabled = True)
    window["-ARGOVALY-"].update(disabled = True)
    window["-ARGPRINTTM-"].update(disabled = True)
    window["-ARGPRINTTX-"].update(disabled = True)
    window["-ARGPRINTWTM-"].update(disabled = True)
    window["-ARGPRINTWTX-"].update(disabled = True)
    window["-ARGCURSORPX-"].update(disabled = True)
    window["-ARGCURSORPY-"].update(disabled = True)
    window["-SHORT1-"].update(disabled = True)
    window["-SHORT2-"].update(disabled = True)
    window["-ARGCURSORMX-"].update(disabled = True, value = "0.0")
    window["-ARGCURSORMY-"].update(disabled = True)
    window["-SHORT3-"].update(disabled = True)
    window["-ARGFLASH-"].update(background_color = "gray", disabled = True)
    window["-ARGFLASHT-"].update(background_color = "gray", disabled = True)
    window["-ARGFLASHD-"].update(background_color = "gray", disabled = True)
    window["-ARGLINEW-"].update(background_color = "gray", disabled = True)
    window["-ARGCLEARL-"].update(disabled = True)
    window["-ARGCOLOR-"].update(background_color = "gray", disabled = True)
    window["-ARGCOLORT-"].update(background_color = "gray", disabled = True)
    window["-ARGCOLORD-"].update(background_color = "gray", disabled = True)
    window["-ARGFONT-"].update(background_color = "gray", disabled = True)
    window["-ARGJUST-"].update(background_color = "gray", disabled = True)
    window["-ARGCOLORB-"].update(background_color = "gray", disabled = True)
    window["-COLORT-"].update(text = "Set the text color >>>", disabled = False)

    #reset ADD buttons
    window["-ADDCOMMENT-"].update(disabled = True, visible = False)
    window["-ADDSPACE-"].update(disabled = True, visible = False)
    window["-ADDCURSORP-"].update(disabled = True, visible = False)
    window["-ADDCURSORM-"].update(disabled = True, visible = False)
    window["-ADDCOLOR-"].update(disabled = True, visible = False)
    window["-ADDCOLORT-"].update(disabled = True, visible = False)
    window["-ADDCOLORD-"].update(disabled = True, visible = False)
    window["-ADDFLASH-"].update(disabled = True, visible = False)
    window["-ADDFLASHT-"].update(disabled = True, visible = False)
    window["-ADDFLASHD-"].update(disabled = True, visible = False)
    window["-ADDFONT-"].update(disabled = True, visible = False)
    window["-ADDJUST-"].update(disabled = True, visible = False)
    window["-ADDCOLORB-"].update(disabled = True, visible = False)
    window["-ADDCOLORBG-"].update(disabled = True, visible = False)
    window["-ADDLINEW-"].update(disabled = True, visible = False)
    window["-ADDLINE-"].update(disabled = True, visible = False)
    window["-ADDOVAL-"].update(disabled = True, visible = False)
    window["-ADDPRINT-"].update(disabled = True, visible = False)
    window["-ADDPRINTW-"].update(disabled = True, visible = False)
    window["-ADDCLEAR-"].update(disabled = True, visible = False)
    window["-ADDCLEARL-"].update(disabled = True, visible = False)

    #reset description texts 
    window["-scpt-"].update(" ")
    window["-desc-"].update(" ")
    window["-synt-"].update(" ")
    window["-exem-"].update(" ")
    window["-flashms-"].update(" ")
    window["-flashmst-"].update(" ")
    window["-flashmsd-"].update(" ")
    window["-flashhex-"].update(" ")
    window["-flashhext-"].update(" ")
    window["-flashhexd-"].update(" ")

def clear_image(window, image1, image2, image3, image4, image5, image6, image7, image8):
    try:
        window["-graph-"].delete_figure(image1)
        window["-graph-"].delete_figure(image2)
        window["-graph-"].delete_figure(image3)
        window["-graph-"].delete_figure(image4)
        window["-graph-"].delete_figure(image5)
        window["-graph-"].delete_figure(image6)
        window["-graph-"].delete_figure(image7)
        window["-graph-"].delete_figure(image8)
    except:
        pass
   
def get_color_hex(index):
    hex_color = ListOfColorsHex[index]
    return(hex_color)

def get_flash_hex(index):
     print("flash func index: ", index)
     hex_flash = ListOfFlashHex[index]
     print("flash func hex: ", hex_flash)
     return(hex_flash)

def get_width_float(index):
     print("width func index: ", index)
     float_width = ListOfWidthFloat[index]
     print("width func float: ", float_width)
     return(float_width)

def get_text_integer(index):
     value_font = ListOfFontInt[index]
     print("font size integer value: ", value_font)
     return(value_font)

def get_BG_integer(index):
     value_BG = ListOfSwitchInt[index]
     print("BG switch integer value: ", value_BG)
     return(value_BG)

def get_On_Off(string):
    if string == "ON":
        status = 2
    elif string == "OFF":
        status = 0
    return status

def get_radians(index):
    radians_degrees = range(-360, 361, 5)
    #Convert and round to 4 decimal places
    radians_list = [round(radians(d), 4) for d in radians_degrees]
    print("Get Radians list: ", radians_list)
    radian_value = radians_list[index]
    print("Radian value: ", radian_value)
    return str(radian_value)

def get_width(index):
    print ("width list index: ", index)
    if index == 0:
        return 0.1
    if index == 1:
        return 0.5
    if index == 2:
        return 1
    if index == 3:
        return 1
    if index == 4:
        return 2
    if index == 5:
        return 3
    if index == 6:
        return 5
    if index == 7:
        return 20
    if index == 8:
        return 40
    if index == 9:
        return 60
    if index == 10:
        return 100
    if index == 11:
        return 200

def make_coordinates():
    for i in range(100, -101, -1):
        value = i / 100.00
        formatted_value = f"{value:.2f}"
        coord_list.append(formatted_value)
    print("=>functions/coord: ", coord_list)
    return coord_list

def disable_button(window, key):
    print("Enable button: ", key)
    window[key].update(disabled = True)

def enable_button(window, key):
    print("Disable button: ", key)
    window[key].update(disabled = False)

def get_description(window, script, description, example, syntax):
    window["-scpt-"].update(script)
    window["-desc-"].update(description)
    window["-synt-"].update(example)
    window["-exem-"].update(syntax)

def clear_description(window):
    window["-scpt-"].update(" ")
    window["-desc-"].update(" ")
    window["-synt-"].update(" ")
    window["-exem-"].update(" ")
  
#configure SCRIPT and SUMMARY input
def Handle_Function(window, list1, list2, list3, list4, script, summary, arg1, arg1a, arg2):
        print(">>Handle Functions arg1: ", arg1)
        print(">>Handle Functions arg1a: ", arg1a)
        print(">>Handle Functions arg2: ", arg2)
        #clears and appends the new script and summary to the lists
        list1.clear()
        list1.append(script)
        list2.clear()
        list2.append(summary)
        #arg1 = 1st script argument and arg1a = 1st for summary
        if arg1 != None:
            if script == "Print" or script == "WaitPrint" or script == "SetCursor" or script == "MoveCursor" or script == "SetPanTilt" or script == "MovePanTilt":
                list1.append(arg1)
                list1.append(arg1a)
                list2.append(arg1)
                list2.append(arg1a)
            else:
                list1.append(arg1)
                list2.append(arg1a)
        if arg2 != None:
            list1.append(arg2)
            list2.append(arg2)
        #sets the SCRIPT section
        list3.append(list1.copy())
        window["-SCRIPT-"].update(values = list3)
        #sets the SUMMARY section
        list4 = " ".join(list2)
        window["-FILE_TEXT-"].write(list4 + "\n")
        #create logs
        print(">>Handle Functions - script: ", list3)
        print(">>Handle Functions - summary: ", list4)

def Draw_Lines(window, values):
    list_temp = []
    a = 0.15
    b = 0.21
    c = 1
    for i in range(5):
        window["-graph-"].draw_line((-0.80, a), (-0.20, a), values, width = c)
        list_temp.append(window["-graph-"].draw_line((-0.80, a), (-0.20, a), values, width = c))
        window["-graph-"].draw_line((a, 0.40), (a, -0.40), values, width = c)
        list_temp.append(window["-graph-"].draw_line((a, 0.40), (a, -0.40), values, width = c))
        a = a - 0.15
        b = b - 0.15
        c = c + 1
    return(list_temp)

 #return callback

def Get_Callbacks():
        pass

#sort the type of file (txt, run) extension to be displayed
def extension_to_be_displayed (_folder, _txt, _run, _all):
    list_of_files_in_folder = os.listdir(_folder)
    if _txt:
        selected_file_extension = [f for f in list_of_files_in_folder if os.path.isfile(os.path.join(_folder, f)) and f.lower().endswith((".txt"))]
    elif _run:   
        selected_file_extension = [f for f in list_of_files_in_folder if os.path.isfile(os.path.join(_folder, f)) and f.lower().endswith((".run"))]
    elif _all:  
        selected_file_extension = [f for f in list_of_files_in_folder if os.path.isfile(os.path.join(_folder, f)) and f.lower().endswith((".txt", ".run", ".bkp"))]
    else:
        sg.popup("You must select a type of extension!", no_titlebar = True, any_key_closes = True, keep_on_top = True, modal = True)
    return selected_file_extension

#get list of all .txt files to be displayed
def extension_txt (_folder):
    list_of_files_in_folder = os.listdir(_folder)
    selected_txt_extension = [f for f in list_of_files_in_folder if os.path.isfile(os.path.join(_folder, f)) and f.lower().endswith((".txt"))]
    return selected_txt_extension

#convert list of integers to list of strings
def get_string_integer(_list):
    list_string = list(map(str, _list))
    return list_string

    
