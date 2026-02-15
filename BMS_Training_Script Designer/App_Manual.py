#import PySimpleGUI as sg
import FreeSimpleGUI as sg
import App_Images




def manual_comment(function):
    if function == "-COMMENT-":
        sg.popup_scrolled("""
                         Function: // 
                         Syntax: // text
                         Example: // This is a comment. 

        Description: Any text starting with // will be ignored by the script.""",
                        title = "BMS Techincal Manual Chapter 14.", size = (100,10), button_justification = "c", modal = True, keep_on_top = True)
    elif function == "-SPACE-":
        sg.popup_scrolled("""
                         Function: none 
                         Syntax: none
                         Example: none

        Description: Just an empty line.""",
                        title = "BMS Techincal Manual Chapter 14.", size = (100,10), button_justification = "c", modal = True, keep_on_top = True)
    elif function == "-CURSORP-":
        sg.popup_scrolled("""
                         Function: SetCursor 
                         Syntax: SetCursor <float (x)> <float (y)> 
                         Example: SetCursor 0.0 0.95 

        Description: Sets the cursor position to the location specified in <float (x)> and <float (y)>. 
        The range of the coordinate system is from -1.0 to 1.0. For example x = -1.0 is the left of the screen, 
        0.0 is the center and 1.0 is the right side of the screen. This cursor location is used for all 
        print and draw functions. The cursor position stays the same all the time until it is 
        relocated to another screen location by using either SetCorsor or MoveCursor""",
                        title = "BMS Techincal Manual Chapter 14.5.1", size = (100,10), button_justification = "c", modal = True, keep_on_top = True)
    elif function == "-CURSORM-":
        sg.popup_scrolled("""
                         Function: MoveCursor 
                         Syntax: MoveCursor <float (x)> <float (y)> 
                         Example: MoveCursor 0.0 -0.05 

        Description: Moves the cursor from its current position by x and y amount. The range of the 
        coordinate system is from -1.0 to 1.0. For example x = -1.0 is the left of the screen, 0.0 is 
        the center and 1.0 is the right side of the screen. This cursor location is used for all print 
        and draw functions. The cursor position stays the same all the time until it is relocated 
        to another screen location by using either SetCorsor or MoveCursor.""",
                        title = "BMS Techincal Manual Chapter 14.5.1", image = App_Images.movecursor_image, size = (100,10), button_justification = "c", modal = True, keep_on_top = True)
    elif function == "-COLOR-":
        sg.popup_scrolled("""
                        Function: SetColor
                        Syntax: SetColor <hex> 
                        Example: SetColor 0xFFFFFFFF 

        Sets the current cursor color to the color specified by <hex>. This cursor color is used for 
        all print and draw functions. The setting affects all following draw & text functions until 
        another value is defined either using SetColor, SetFontColor or SetDrawColor. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-COLORT-":
        sg.popup_scrolled("""
                        Function: SetFontColor
                        Syntax: SetFontColor <hex> 
                        Example: SetFontColor 0xFFFFFFFF 

        Sets the current cursor color to the color specified by <hex>. This cursor color is used for 
        all print functions. The setting affects all following text functions until 
        another value is defined either using SetColor, SetFontColor or SetDrawColor.  """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,15), modal = True, keep_on_top = True)
    elif function == "-COLORD-":
        sg.popup_scrolled("""
                        Function: SetDrawColor
                        Syntax: SetDrawColor <hex> 
                        Example: SetDrawColor 0xFFFFFFFF 

        Sets the current cursor color to the color specified by <hex>. This cursor color is used for 
        all draw functions. The setting affects all following draw functions until 
        another value is defined either using SetColor, SetFontColor or SetDrawColor.  """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,15), modal = True, keep_on_top = True)
    elif function == "-FLASH-":
            sg.popup_scrolled("""
                        Function: SetFlash
                        Syntax: SetFlash <hex> 
                        Example: SetFlash 0x100

            Sets the rate of flashing that should occur for all text and draw functions. "SetFlash 0" 
            disables flashing. The higher the number (in milliseconds) behind 0x is, the slower the 
            flashing interval is (e.g. 0x100 = 100 ms = fast flashing / 0x900 = 900 ms = slow flashing). 
            The setting affects all following draw & text functions until another value is defined. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True) 
    elif function == "-FLASHT-":
            sg.popup_scrolled("""
                        Function: SetFontFlash
                        Syntax: SetFontFlash <hex> 
                        Example: SetFontFlash 0x100

            Sets the rate of flashing that should occur for all text functions. "SetFlash 0" 
            disables flashing. The higher the number (in milliseconds) behind 0x is, the slower the 
            flashing interval is (e.g. 0x100 = 100 ms = fast flashing / 0x900 = 900 ms = slow flashing). 
            The setting affects all following text functions until another value is defined. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True) 
    elif function == "-FLASHD-":
            sg.popup_scrolled("""
                        Function: SetDrawFlash
                        Syntax: SetDrawFlash <hex> 
                        Example: SetDrawFlash 0x100

            Sets the rate of flashing that should occur for all draw functions. "SetFlash 0" 
            disables flashing. The higher the number (in milliseconds) behind 0x is, the slower the 
            flashing interval is (e.g. 0x100 = 100 ms = fast flashing / 0x900 = 900 ms = slow flashing). 
            The setting affects all following draw functions until another value is defined. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-FONT-":
            sg.popup_scrolled("""
                        Function: SetFont
                        Syntax: SetFont <integer> 
                        Example: SetFont 1

            Sets the font size specified by <integer>. This setting is used for all following print 
            functions until another value is defined. The following values are valid:  
            0 = default font size, bold 
            1 = bigger font size, bold 
            2 = default font size """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-JUST-":
            sg.popup_scrolled("""
                        Function: SetTextOrientation
                        Syntax: SetTextOrientation <integer> 
                        Example: SetTextOrientation 2

            Sets the orientation of the text relative to the cursor position. Acceptable values are 0, 
            1 and 2. 0 = left justified text, 1 = centered text, 2 = right justified text. This function 
            affects all following print functions until another value is defined. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", image = App_Images.justification_image, button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-LINEW-":
            sg.popup_scrolled("""
                        Function: SetLineWidth
                        Syntax: SetLineWidth <float> 
                        Example: SetLineWidth 0.01 

            This sets the line width defined as a floating point number from 0 to 1. Default = 0.005. 
            This setting is used for all following draw functions until another value is defined. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", image = App_Images.width_image, button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-LINE-":
            sg.popup_scrolled("""
                        Function: Line 
                        Syntax: Line <time> <float (x1)> <float (y1)> <float (x2)> <float (y2)> 
                        Example: Line 40 0.55 -0.10 0.75 -0.50

            Draws a line for <time> duration from x1, y1 to x2, y2 coordinates. This function is not 
            dependent from the current cursor location. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-OVAL-":
                sg.popup_scrolled("""
                        Function: Oval
                        Syntax: Oval <time> <float (radius x)> <float (radius y) optional> 
                        Example: Oval 40 0.05 (circle) - Oval 40 0.1 0.05 (oval) 

            Draws an oval on the screen for <time> duration at the current position of the cursor. 
            The size of the oval is specified by the two arguments <float (x)> and <float (y)>. If only 
            one argument is supplied, then a circle is drawn with that radius specified by <float (x)>. 
            The cursor position is at the bottom of the object (marked by the white x), not in its 
            center. """,
                        title = "BMS Techincal Manual Chapter 14.5.3", image = App_Images.oval_image, button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-PRINT-":
                sg.popup_scrolled("""
                        Function: Print
                        Syntax: Print <time> <string>
                        Example: Print 20 "Hello World"

            Prints a string to the screen using the current cursor settings for the duration of <time>. 
            Execution moves immediately onto the next command while leaving the message printed for the duration. 
            Note: If you have not defined the location on the screen (see SetCursor), the message 
            appears in the centre of the screen (0.0 0.0).""",
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-PRINTW-":
                sg.popup_scrolled("""
                        Function: WaitPrint
                        Syntax: WaitPrint <time> <string>
                        Example: WaitPrint 40 "Hello World"

            Prints a string to the screen using the current cursor settings for the duration of <time>. 
            Execution moves immediately onto the next command while leaving the message printed for the duration.
            Functions identically to "Print" except that the execution does not advance to the next 
            command until <time> has expired. 
            Note: If you have not defined the location on the screen (see SetCursor), the message 
            appears in the centre of the screen (0.0 0.0). """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,15), modal = True, keep_on_top = True)
    elif function == "-CLEAR-":
                sg.popup_scrolled("""
                        Function: Clear
                        Syntax: Clear
                        Example: Clar

            Immediately removes all drawn elements from the screen 
            (Such as those created by "Print" "Line" and "Oval" statements). """,
                        title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)
    elif function == "-CLEARL-":
                sg.popup_scrolled("""
                        Function: ClearLast
                        Syntax: ClearLast <integer> (optional)
                        Example: ClearLast 2

            If no argument is provided, the last created drawn element will be removed from the 
            screen (Such as those created by "Print" "Line" and "Oval" statements). If a number is 
            specified, then the nth last element will be removed. For example, "ClearLast 2" will 
            remove the second to last drawn element from the screen. """,
                            title = "BMS Techincal Manual Chapter 14.5.3", button_justification = "c", size = (100,10), modal = True, keep_on_top = True)








    elif function == "-coord-":
            sg.popup_scrolled("""
                            Screen Coordinates / Cursor Position:
            The screen is divided in coordinates. Each coordinate is composed of a set of two floating point numbers, 
            which represent the x- and y-axis. The first number represents the x-axis (left-right) the second one the y-axis 
            (up-down). Both axis values are divided by a blank character (x.x y.y).
            Example: SetCursor 0.0 0.95
            The first number (0.0) is the position on the x-axis, the second (0.95) is the position on the y-axis. 
            Positive numbers move the cursor right (x-axis) or up (y-axis). 
            Negative numbers move the cursor left (x-axis) or down (y-axis). 
            This coordinate system is completely independent of the screen resolution. This ensures, 
            every pilot, no matter of his screen setup, sees the very same result. 
            Whenever you want to type or draw something on the screen, you can move your cursor to a specific position, 
            where the action should occur. If no cursor position is defined, the output will appear on the centre of the screen 
            (0.0 0.0). Instead of writing 0.0 you can also write just 0. """,
                            title = "BMS Techincal Manual Chapter 14.3", image = App_Images.coordinate_image, size = (110,20), button_justification = "c", modal = True, keep_on_top = True)
    elif function == "-argm-":
            sg.popup_scrolled("""
                            Functions and Arguments: 
            Each function can have one or more arguments. Functions and arguments are separated by a blank character. 
            The following is a list of all types of arguments accepted by the system. 
            <time> A floating point number. E.g. 1.0 is 1 second, 0.001 is 1 millisecond. 
            <integer> A whole number like 1 or 2. 
            <float> A floating point number, e.g. 1.0 / -0.25 / 0.5 / -0.05 etc. 
            <string> A string of characters surrounded with quote marks.  
            <hex> A hexadecimal number which sets a color, like 0xffffffff (=white). 
            <command> The name of command as found in the keystrokes files. An example is SimTogglePaused. 
            <section> The name of a section in the script. """,
                            title = "BMS Techincal Manual Chapter 14.4", button_justification = "c", size = (110,15), modal = True, keep_on_top = True)
