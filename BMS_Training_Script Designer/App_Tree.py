import FreeSimpleGUI as sg
import App_Functions
import App_Images

#Creates sample data mimicking a file system for the Tree element.
#The format is [key, parent_key, text, values_list, icon].
def functions_in_tree():
    functions_in_tree = [
        # Root menu
        ['-CPO-', '', '1. Cursor Positioning', [], App_Images.cursor_image1],
        ['-OUT-', '', '2. Output', [], App_Images.output_image1],
        ['-LAY-', '', '3. Layout', [], App_Images.layout_image1],
        ['-INT-', '', '4. User Interface', [], App_Images.interface_image1],
        ['-SEC-', '', '5. Section', [], App_Images.section_image1],
        ['-SOU-', '', '6. Sound', [], App_Images.sound_image1],
        ['-COP-', '', '7. Cockpit Orientation', [], App_Images.orientation_image1],
        ['-COM-', '', '8. Command & Fault', [], App_Images.command_image1],
        ['-IMS-', '', '9. Initial Mission Setup', [], App_Images.mission_image1],
        ['-TIM-', '', '10. Time Management', [], App_Images.time_image1],
        ['-BOL-', '', '11. Boolean', [], App_Images.boolean_image1],
        ['-OTH-', '', '12. Other Functions', [], App_Images.other_image1],

        # Cursor Positioning contents
        ['-cposet-', '-CPO-', '1.1 Set cursor position', [], App_Images.cursor_image2],
        ['-cpomov-', '-CPO-', '1.2 Move cursor position', [], App_Images.cursor_image2],
        
        # Output contents
        ['-outtxt-', '-OUT-', '2.1 Show TEXT on screen', [], App_Images.output_image2],
        ['-outtxtw-', '-OUT-', '2.2 Show TEXT on screen holding the script for the time', [], App_Images.output_image2],
        ['-outoval-', '-OUT-', '2.3 Show OVAL or CIRCLE on screen', [], App_Images.output_image2],
        ['-outline-', '-OUT-', '2.4 Show LINE on screen', [], App_Images.output_image2],

        # Layout contents
        ['-layall-', '-LAY-', '3.1 Set color to ALL elements', [], App_Images.layout_image2],
        ['-laytxt-', '-LAY-', '3.2 Set color to TEXTS', [], App_Images.layout_image2],
        ['-layshp-', '-LAY-', '3.3 Set color to SHAPES', [], App_Images.layout_image2],
        ['-layfsh-', '-LAY-', '3.4 Make ALL elements blink', [], App_Images.layout_image2],
        ['-layfsht-', '-LAY-', '3.5 Make TEXTS blink', [], App_Images.layout_image2],
        ['-layfshd-', '-LAY-', '3.6 Make SHAPES blink', [], App_Images.layout_image2],
        ['-layfon-', '-LAY-', '3.7 Adjust text size', [], App_Images.layout_image2],
        ['-layjus-', '-LAY-', '3.8 Adjust text justification', [], App_Images.layout_image2],
        ['-layline-', '-LAY-', '3.9 Adjust Line width', [], App_Images.layout_image2],
        ['-laybcg-', '-LAY-', '3.10 Define text background color', [], App_Images.layout_image2],
        ['-laybcgs-', '-LAY-', '3.11 Turn background color on/off', [], App_Images.layout_image2],
        ['-layclr-', '-LAY-', '3.12 Removes all elements from screen', [], App_Images.layout_image2],
        ['-layclrl-', '-LAY-', '3.13 Remove especific elements from screen', [], App_Images.layout_image2],

        # User Interface contents
        ['-intpause-', '-INT-', '4.1 Pause script until command is given', [], App_Images.interface_image2],
        ['-intmouse-', '-INT-', '4.2 Pause script until mouse move over a postition', [], App_Images.interface_image2],
        ['-intblock-', '-INT-', '4.3 Block a specified (or all) command', [], App_Images.interface_image2],
        ['-intallow-', '-INT-', '4.4 Allow a specified (or all) command', [], App_Images.interface_image2],

         # Section contents
        ['-secname-', '-SEC-', '5.1 Name a section', [],App_Images.section_image2],
        ['-secjmp-', '-SEC-', '5.2 Jump to a section', [],App_Images.section_image2],
        ['-secjmpi-', '-SEC-', '5.3 Jump to a section if a condition is met', [],App_Images.section_image2],
        ['-secjmpin-', '-SEC-', '5.4 Jump to a section if a condition is not met', [],App_Images.section_image2],
        ['-seccal-', '-SEC-', '5.6 Call a section and return', [],App_Images.section_image2],
        ['-seccali-', '-SEC-', '5.7 Call a section and return if a condition is met', [],App_Images.section_image2],
        ['-seccalin-', '-SEC-', '5.8 Call a section and return if a condition is not met', [],App_Images.section_image2],
        ['-secwhl-', '-SEC-', '5.8 Run the commands while value is true', [],App_Images.section_image2],
        ['-secwhln-', '-SEC-', '5.9 Run the commands while value is not true', [],App_Images.section_image2],
        ['-secend-', '-SEC-', '5.10 Set the end of the section', [],App_Images.section_image2],

         # Sound contents
        ['-souply-', '-SOU-', '6.1 Play a sound', [], App_Images.sound_image2],
        ['-souwait-', '-SOU-', '6.2 Play a sound and pause the script', [], App_Images.sound_image2],
        ['-soustop-', '-SOU-', '6.3 Play a sound, pause the script for a time or sound stops', [], App_Images.sound_image2],

         # Cockpit orientation contents
        ['-coppan-', '-COP-', '7.1 Make 3d view look to a direction', [], App_Images.orientation_image2],
        ['-copmove-', '-COP-', '7.2 Make 3d view look offset from its current position', [], App_Images.orientation_image2],
        ['-cophil-', '-COP-', '7.3 Highlight a 3d button/knob in the cockpit', [], App_Images.orientation_image2],
        ['-cophilt-', '-COP-', '7.4 Highlight a 3d button/knob in the cockpit - script paused', [], App_Images.orientation_image2],

         # command and fault contents
        ['-comsim-', '-COM-', '8.1 Execute a BMS command', [], App_Images.command_image2],
        ['-compre-', '-COM-', '8.2 Execute a BMS command when pressing a key', [], App_Images.command_image2],
        ['-comrel-', '-COM-', '8.3 Execute a BMS command when releasing a key', [], App_Images.command_image2],
        ['-comfal-', '-COM-', '8.4 Execute an individual aircraft fault', [], App_Images.command_image2],
        ['-comfalc-', '-COM-', '8.5 Clear an individual aircraft fault', [], App_Images.command_image2],

         # initial mission contents
        ['-ims65-', '-IMS-', '9.1 Set your desired warm up time for AGM-65', [], App_Images.mission_image2],
        ['-imsgun-', '-IMS-', '9.2 Set your desired amount of cannon rounds', [], App_Images.mission_image2],
        ['-imsfuel-', '-IMS-', '9.3 Set your desired amount of fuel', [], App_Images.mission_image2],

        # time management contents
        ['-timwtr-', '-TIM-', '10.1 Pause the script for an amount of REAL time', [], App_Images.time_image2],
        ['-timwtg-', '-TIM-', '10.2 Pause the script for an amount of GAME time', [], App_Images.time_image2],
        ['-timwow-', '-TIM-', '10.3 Pause the script until the aircraf gets airborne', [], App_Images.time_image2],

        # boolean contents
        ['-bolif-', '-BOL-', '11.1 Check if the value of last command is true', [], App_Images.boolean_image2],
        ['-bolifn-', '-BOL-', '11.2 Check if the value of last command is not true', [], App_Images.boolean_image2],

        # others contents
        ['-othcom-', '-OTH-', '12.1 Add a comment line to the script', [], App_Images.other_image2],
        ['-othline-', '-OTH-', '12.2 Add a blank line (space) to the script', [], App_Images.other_image2],
        ['-othends-', '-OTH-', '12.3 End the script', [], App_Images.other_image2],
        ['-othent-', '-OTH-', '12.4 Enter Critical (avoid it, very dangerous)', [], App_Images.other_image2],
        ['-othend-', '-OTH-', '12.5 End Critical (avoid it, very dangerous)', [], App_Images.other_image2],
    ]
    return functions_in_tree

#Handles the selection of an item in the Tree element.
def handle_tree_selection(window, selected):
    App_Functions.clear_description(window)
    App_Functions.disable_button(window,"-BADD-")
    App_Functions.disable_button(window,"-BPAR-")
    App_Functions.disable_button(window,"-BHEL-")

    print("selected tree functions: ", selected)
    #Name a section
    if selected == "-secname-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.get_description(window, "Name of your section", "Name a section where your script can return to.", "Difine a name section.", "Use sections when you need your script to repeat or jump some functions. DO NOT FORGET TO END THE SECTION! (function 5.10)")
    #End Section function
    elif selected == "-secend-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "EndSection", "This function can be used to end a section.", "EndSection", "End the section so functions like <While>, <WhileNot>, <Call>, <Jump> and others know when to stop.")
    #Clear all elements function
    elif selected == "-layclr-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "Clear", "Immediately removes all drawn elements from the screen.", "Clear", "Use when you want to erase all elements at once from the screen.")
    #Clear last n element function
    elif selected == "-layclrl-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "ClearLast", "The last created <n> drawn elements will be removed.", "ClearLast <Integer> (optional)", "Use 0 if you just want to erase the last element from the screen.")
    #While function
    elif selected == "-secwhl-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "While", "If the prior return value is TRUE, runs the commands until the next <EndSection>.", "While", "As an example, a block of script continues to run while the Landing Gear is up.")
    #While Not function
    elif selected == "-secwhln-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "WhileNot", "If the prior return value is FALSE, runs the commands until the next <EndSection>.", "WhileNot", "As an example, a block of script continues to run while the Landing Gear is not up.")
    elif selected == "-othends-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "EndScript", "Immediately ends the script. All following functions will be ignored.", "EndScript", "Although it is a good habit to end the script, it is not needed to do so.")
    elif selected == "-othent-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "EnterCritical", "This experimental function can be used to execute multiple commands in a single frame.", "EnterCritical", "It is not advised to use this function as there is really no need to do so!")
    elif selected == "-othend-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "EndCritical", "This function cancel <EnterCritical> and causes one command per frame execution to resume.", "EndCritical", "It is not advised to use <EnterCritical> and <EndCritical> functions.")
    elif selected == "-bolif-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "If", "If the return value of the last command is TRUE, then execution moves to the next instruction.", "If", "As an example, if you command the LG down (and it works), next script line (message: have a good landing!) will show.")
    elif selected == "-bolifn-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "IfNot", "If the return value of the last command is FALSE, then execution moves to the next instruction.", "IfNot", "As an example, if you command the LG down (and it does not work), next script line (message: have a good landing!) will not show.")
    elif selected == "-timwow-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window, "WaitForNoWOW", "This prevents the script from continuing for an unspecified amount of time until an aircraft gets airborne (No Weight-On-Wheels).", "WaitForNoWOW", "Use when you want your script to start after aircraft takes off.")
    elif selected == "-othcom-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "C/C++ comment symbol // followed by a text", "Add a comment that will be ignored by the script.", "Just write anything you want.", "It is important to comment your script. At least an introduction about what it does.")
    elif selected == "-othline-":
        App_Functions.enable_button(window,"-BADD-")
        App_Functions.get_description(window,  "Empty Line (space)", "Add an empty line to separate different sections of the script.", "Nothing.", "Separate parts of your script using space to help it became more readble.")
    elif selected == "-layall-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetColor <hex>", "Define a color for all draw and text objects.", "Pick a color that suits your needs.", "Its a good idea to use different colors for diferent contexts.")
    elif selected == "-laytxt-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetFontColor <hex>", "Sets the color of the text only.", "Pick a color that suits your needs.", "Its a good idea to use different colors for diferent contexts.")
    elif selected == "-layshp-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetDrawColor <hex>", "Sets the color of lines and ovals only.", "Pick a color that suits your needs.", "Its a good idea to use different colors for diferent contexts.")
    elif selected == "-laybcg-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetFontBGColor <hex>", "Sets the background color of the text. The default is transparent.", "Pick a color that suits your needs.", "Use background colors to highlight important information.")
    elif selected == "-layfsh-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetFlash <hex>", "Sets the rate of flashing that should occur for all text and draw functions.", "Pick a flash rate that suits your needs", "Use flash with caution as this may turn the enviroment tiresome.")
    elif selected == "-layfsht-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetFontFlash <hex>", "Sets the rate of flashing that should occur for texts functions.", "Pick a flash rate that suits your needs", "Use flash with caution as this may turn the enviroment tiresome.")
    elif selected == "-layfshd-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetDrawFlash <hex>", "Sets the rate of flashing that should occur for draw functions.", "Pick a flash rate that suits your needs", "Use flash with caution as this may turn the enviroment tiresome.")
    elif selected == "-layfon-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetFont <integer>", "Sets the font size specified by the given number.", "Options are: 0 - default size bold, 1 - bigger size bold, 2 - default size.", "Use bigger size to emphasize important messages.")
    elif selected == "-layjus-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetTextOrientation <integer>", "Sets the orientation of the text relative to the cursor position.", "Acceptable values are 0 = left justified text, 1 = centered text, 2 = right justified text.", "Be careful not to make your text goes off the screen.")
    elif selected == "-layline-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetLineWidth <float>", "Sets the line width defined by the given number.", "Enter float number from 0.001 to 1.0. Default value is 0.005.", "This graphic limits the line sample width to 0.1 - you will see why ;)")
    elif selected == "-laybcgs-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetTextBoxed <Integer>", "Sets the type of text boxing that should apply to print statements.", "Switch text boxing ON or OFF.", "Use background colors to highlight important information.")
    elif selected == "-imsgun-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetGunAmmo <Integer>", "Sets the amount of cannon rounds.", "Define a number from 0 to 99.999 (value limited only by this app).", "Use this functions when you want to practice cannon shots.")
    elif selected == "-ims65-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetMavCoolTime <Float>", "This function sets the Mavergick's spool up time in seconds. Default is 180.0 (3min).", "Define a number from 0.0 to 999.9 (value limited only by this app).", "Good way to reduce Mav spool up time. (My guess is that you don't want to increase it)")
    elif selected == "-imsfuel-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetFuel <Integer1>... <Integer14>", "This function sets the fuel capacity for each fuel compartment independently.", "Define the amount of fuel for each tank (values rounded by this app).", "Pre-defined limits desinged for F16 only.  Later updates will include more aircrafts.")
    elif selected == "-timwtr-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "Wait <Time>", "Pauses execution of the script until the specific REAL <time> expires.", "Define the amount of real time (your clock) you want the script to be paused.", "In game pause DOESN'T interrupt this function.")
    elif selected == "-timwtg-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "WaitGameTime <Time>", "Pauses execution of the script until the specific GAME <time> expires.", "Define the amount of real time (BMS clock) you want the script to be paused.", "In game pause DO interrupt this function. Freeze DOESN'T.")
    elif selected == "-soustop-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "WaitSoundStop <Time>", "Pauses execution of the script for <time> duration or until the last sound stops playing.", "Define the amount of time you want the script to be paused.", "This is a good function if you wish to implement recorded instructions.")
    elif selected == "-outtxt-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "Print <Time> <String>", "Shows a text using the current cursor settings for the duration of <time>. Script moves onto the next command.", "Define the amount of time the script will be paused and the text to be shown on the screen.", "Don't forget to set the coordinates to where you want the text to appear.")
    elif selected == "-outtxtw-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "WaitPrint <Time> <String>", "Shows a text using the current cursor settings for the duration of <time>. Script does not move to the next command until <time>.", "Define the amount of time the script will be paused and the text to be shown on the screen.", "Don't forget to set the coordinates to where you want the text to appear.")
    elif selected == "-cposet-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetCursor <float (x)> <float (y)>", "Sets the cursor position to the location specified  in <float (x)> and <float (y)>.", "If no coordinate is defined, the default is the center of the grid (0.00 , 0.00).", "A good place to start a text is at:  -0.98(x) 0.08(y)")
    elif selected == "-cpomov-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "MoveCursor <float (x)> <float (y)>", "Moves the cursor from its current position by x and y amount.", "The cursor position stays the same until it is relocated by using either SetCursor or MoveCursor.", "A good cursor movement for texts is: 0.00(x) -0.04(y)")
    elif selected == "-coppan-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "SetPanTilt <float (x)> <float (y)>", "Sets the current 3d view to the coordinates specified by <float (x)> and <float (y)>.", "Choose how many degrees you want the view to tilt horizontally and vertically.", "0.0 degrees is straight ahead. Positive numbers move left or down.")
    elif selected == "-copmove-":
        App_Functions.enable_button(window,"-BPAR-")
        App_Functions.enable_button(window,"-BHEL-")
        App_Functions.get_description(window, "MovePanTilt <float (x)> <float (y)>", "Offsets the current 3d view from its current position by the amounts specified by <float (x)> and <float (y)>.", "Choose how many degrees you want the view to move horizontally and vertically.", "Positive numbers move left or down. Negative numbers move right or up.")



