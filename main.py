# Importing of Libraries

from colors import *
from time import sleep
import subprocess
import os

# Player Variables

player_name = ""
player_money = 1000

# Clear Function of easy usage

def clear():

    if os.name == 'nt':

        _ = os.system('cls')

    else:

        _ = os.system('clear')

# Quit menu for easy usage

def quit_menu():

    while True:

        print("Are you sure you want to quit")

        ch = str(input("> "))

        if ch == 'y':

            print("Thanks for playing")

            sleep(2)

            exit(0)

        else: 

            break    

# Mini Game Code

def minigame():

    while True:

        clear()

        print("How much bet do you want to keep")

        bet = int(input("> "))

        if bet > player_money:

            print("Do you want to have debt is it?")


# menu whenever who come to a port

def port_menu():

    print("Press the Corresponding key to go to different places")

    print("SHOP")

    print("PUB")

    print("SAIL")

# Shop Menu

def shop():

    while True:

        clear()

        print("You are now going to the shop")

        sleep(2)

        clear()

        print("You are now in the shop")

        print("You can buy goods from here")

        print("List of goods")

        print("Animal Skins")

        print("Harpoons")

        print("Food")

        print("Cannons")

        print("Cannon balls")

        ch = str(input("> "))

        ch = ch.lower()

        if ch == 'b':

            break

        elif ch == 'q':

            quit_menu()

# Pub Menu

def pub():

    while True:

        clear()

        print("You are going to the pub")

        print("You can get missions from here or play a gambling game")

        print("What you want to do")

        ch = str(input("> "))

        ch = ch.lower()

        if ch == 'b':

            break

        elif ch == 'q':

            quit_menu()

        elif ch == 'g':

            pass

# Sail Mini Game

def sail():

    pass

# Main Game Loop

def main():

    while True:

        clear()

        port_menu()

        ch = str(input("> "))

        ch = ch.lower()

        if ch == 'q':

            quit_menu()

        elif ch == 's':

            shop()

        elif ch == 'p':

            pub()

# Start of the game (separated from the main function because it is only one time use)

print("Press P to play and Q to quit")

ch = str(input("> "))

if ch == 'q':

    exit(0)
        
elif ch == 'p':

    clear()

    print("Starting..........")

    sleep(2)

else:

    print("Invaild Argument")

subprocess.run(['python' , './intro.py'])

player_name = str(input("Enter your character name: "))

print("Your character name: " , player_name)

sleep(2)

main()
