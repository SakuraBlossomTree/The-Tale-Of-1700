from colorama import Fore , Back , Style , init , deinit
from colors import *
from time import sleep
import os

def clear():

    if os.name == 'nt':

        _ = os.system('cls')

    else:

        _ = os.system('clear')

def text_centered(text):

    terminal_size = os.get_terminal_size()

    width = terminal_size.columns

    height = terminal_size.lines

    hor_pad = (width - len(text)) // 2

    ver_pad = (height // 2) - 1

    for _ in range(ver_pad):

        print()

    print(COLOR_BLUE + COLOR_STYLE_BRIGHT + " " * hor_pad + text)

    print(COLOR_RESET_ALL)

clear()

text_centered("A GAME MADE BY A 19 YEAR OLD")

sleep(2)

clear()

text_centered("THE TALE OF 1700 BY SAKURABLOSSOMTREE")

sleep(2)

clear()

print("It is the late 1700, where the war rages on")

print("The English are allied with the French for now and the Spains's rule the waters")

print("Can you survive the waters of the carribiean sea")