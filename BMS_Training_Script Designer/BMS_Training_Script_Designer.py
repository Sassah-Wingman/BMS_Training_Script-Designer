# This is a application designed to convert .dat files to proto for Falcon BMS 
# using Pysimplegui 3.17.
# Sao Paulo, Brazil
# jul 2024
#__version__ = "1.0 - jul 2024"

PySimplegGUI_Licence = "ezy7J1MRaJWUNAlcbYnrN2l8VcHUl1whZbSCIl6aIMkYR7pgch3eRhyKaWWqJs1KdHGLlRvVbNiFI8sZI4kbxVpSYx2zVhuOct27VCJdR3CzI96rMaT0cq0eNEzZA2wsMaz4kh44NIijwwiNT0GvlujUZJWr5uzXZbU5RnlrcaGOx7v7egW51hlBbVnARXWKZaXFJWzzaPW39IuKI6jqonibNhSk4UwPIDiZwYi2TjmXFhtPZ1USZxphcWnvNg0QIqjLoQi0Z33kVHzOdqGPFp2Ub9ylInsIIDkn5mhKbAWbVlMsYBXVNR0OIwj3o9iRbVW2VepAc2mTVyshb7GSV6zkIGigwqiwQm2R9otxcjGZFPuveLSuIv60IBkGdD1Uc43NRThmdZm186gkUa2LF1yLdYGN93yZaMS6IOsGIVkONp15c13xRbv3bNWYVuyLS3UVQhiDOWidIEykOTDwkqynNQCwI0sDI2ktRIhGdXG9VGJzcf3HNV10ZzWKQ4iBOGijI8yRMlDqIV1tLSTRAl1BL5TgE4yeIyiPwiiHRgGhFK0SZOUKVL4ycoGylSyZZYXGMPikOfikIty3MPD1I31gLzTVA23aLdTTAt1ZI1ibwiibRLWL1KhzaKWcxMBMZdGjRAyFZNXvNEzaIPjEoRirZe3CNztdZnWOlwyYZuWKxashZ0XcNcAVZQ2U1AhAafWCwzuEYI2w9utjIditwSiMSuVGBkBsZPGxRPyzZVXjNrzsIJjPosiqMpT5cC56L6jeIOwFOtCr4bxqM1zYkbukMdTlMt3OIgnU04=K2d1f6521d94ee26e2b3b43f5e117c60a948396fedc32c62d2cd1c7bb74e29e205aa909afd1ff53cb83e8087c5200a8c6b290608b536fbeaf982f76e4aa4bec478600895c676ae8637506bec7c962a9d91fdab839cb4181d39aab83cacdd28d254bc168715a6480abe2de1f7c23691c1026d697cd804c857894a649e388045ca721756c580d78799b607835d1dfdc07d6713f4d9a461bf2d6d418a714033e1b9f1e04f276dd8ea110d293e30f95eea9cf0b85333c998429221c0ebed492885cd4cd6650adfa2ade14e491630262946447b12d2c0b4900c24c996d31ed612f3960c9e7de06e9378cc70e74b9e534b1de2a309efbb67e21f07b4e9247222f9bff758384cfd6423d967c35f1744fe09759980a71856d4abf91fcd03b2bcb535b5f7752d23018c5239ca9e1fc0e6538c9a8644c81123887f5ab0123fde618eb9a343959bbd53d7b943ff3e6ae84dfb70a77552eb74296d81ad4e4e76ac241b6466fa0b2a6ac4dc7f71310fc9cb7ec8c9547beec36433171b23f70a0ccc6012c35dd78aca66d494bb20cd2941051f2803d67a5be61466038a5ed9765c81c5c50ec99236030eb58888c9d1c2050e58a4d793268a041396ba65951fd779f7220afba38cceff577a00b1bd68e28f06cda03286754f853ffed778732a6cbc701dfdaa9fce7bae56837f896e69bb88096abf806cd538ec0b74074dbf9a67590cdd40ef96392"
import PySimpleGUI as sg
import os
import sys
#my moodules
import Script_Windows
import Script_Functions
import Script_Images
import module3
import module2

#global configurations
__version__ = "v1.0 - 2024."
sg.set_options(font = "Arial, 10")
BMSBlueGray = {'BACKGROUND': '#91a6be',
             "TEXT": "#000000",
             "INPUT": "#ffffff",
             "TEXT_INPUT": "#000000",
             "SCROLL": "#64778d",
             "BUTTON": ("#ffffff", "#4b586e"),
             "PROGRESS": ("#64778d", "#d4d7dd"),
             "BORDER": 1, 
             "SLIDER_DEPTH": 0, 
             "PROGRESS_DEPTH": 0}
sg.theme_add_new("BMSBlueGray", BMSBlueGray)
sg.theme("BMSBlueGray")

#program entry point
def main():
    module3.start_window()
    
if __name__ == "__main__":    
    main()        

# colors (ligthest to darkest):
#d4d7dd: light gray    
#91a6be: naval light blue
#64778d: naval dark blue
#4b586e: lead dark gray