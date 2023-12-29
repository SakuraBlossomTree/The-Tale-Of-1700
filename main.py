# Importing of Libraries

from colors import *
from time import sleep
import subprocess
import os
import random

# Player Variables

player_name = ""
player_money = 1000

# Goods Value

animal = 25

harpoons = 10

food = 25

jew = 100

cannons = 60

cannon_balls = 10

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

    global player_money

    while True:

        print("Do you want to play the game")

        choice = str(input("> "))

        if choice == 'y':

            clear()

            print("How much bet do you want to keep")

            bet = int(input("> "))

            if bet > player_money:

                print("Do you want to have debt is it?")

                sleep(4)

            else:

                print("Game Starts")

                dice = []

                dealer_dice = []

                i = 1 

                j = 1 

                while i <= 5:

                    player_dice = random.randint(1,6)

                    dice.append(player_dice)

                    i+=1

                while j <= 5:

                    dealer_die = random.randint(1,6)

                    dealer_dice.append(dealer_die)

                    j+=1

                print("Dealer dice: " , dealer_dice)

                sleep(2)

                print("Player dice: " , dice)

                dealer_sum = sum(dealer_dice)

                player_sum = sum(dice)

                sleep(2)

                print(sum(dealer_dice))

                sleep(2)

                print(sum(dice))

                if player_sum > dealer_sum:

                    print("You win!")

                    player_money += bet

                elif dealer_sum > player_sum:

                    print("You lose")

                    player_money -= bet

                else:

                    print("Draw")


        elif choice == 'n':

            break

        else:

            print("Invaild Argument")



# menu whenever who come to a port

def port_menu():

    print("Press the Corresponding key to go to different places")

    print("SHOP")

    print("PUB")

    print("SAIL")

    print("Money: " , player_money)

# Shop Menu

def shop():

    global player_money

    while True:

        clear()

        print("You are now going to the shop")

        sleep(2)

        clear()

        print("You are now in the shop")

        print("You can buy goods from here")

        print("List of goods")

        print("Animal Skins" , animal)

        print("Harpoons" , harpoons)

        print("Food" , food)

        print("Jewellery" , jew)

        print("Cannons" , cannons)

        print("Cannon balls" , cannon_balls)

        ch = str(input("> "))

        ch = ch.lower()

        if ch == 'b':

            print("Press u to buy or a to go back")

            choice = str(input("> "))

            if choice == 'u':

                print("You are buying goods")

                print("1) Animal Skins" , animal)

                print("2) Harpoons" , harpoons)

                print("3) Food" , food)

                print("4) Jewellery" , jew)

                print("5) Cannons" , cannons)

                print("6) Cannon balls" , cannon_balls)

                print("What do you want to buy: ")

                good_choice = int(input("> "))

                match good_choice:

                    case 1:

                        print("Selected Animal Skins")

                        print("How many you want to buy")

                        no_of_food = int(input("> "))

                        print(no_of_food)

                        sleep(2)

                        print(f"Are you sure you want to buy {no_of_food} Animal Skins")

                        choice2 = str(input("> "))

                        if choice2 == 'y':

                            print("okay")

                            player_money = player_money - (no_of_food * animal)

                            if player_money < 0:

                                print("You cannot buy these many Animal Skins")
                                
                                sleep(4)
                                
                                player_money = player_money + (no_of_food * animal)

                            else:

                                print("You are good to go")

                                sleep(2)
                                
                        elif choice2 == 'n':

                            break

                        else:

                            print("Invaild Argument")

                        sleep(2)

                    case 2:

                        print("Selected Harpoons")
                        
                        print("How many you want to buy")

                        no_of_food = int(input("> "))

                        print(no_of_food)

                        sleep(2)

                        print(f"Are you sure you want to buy {no_of_food} Harpoons")

                        choice2 = str(input("> "))

                        if choice2 == 'y':

                            print("okay")

                            player_money = player_money - (no_of_food * harpoons)

                            if player_money < 0:

                                print("You cannot buy these many Harpoons")
                                
                                sleep(4)
                                
                                player_money = player_money + (no_of_food * harpoons)

                            else:

                                print("You are good to go")

                                sleep(2)
                                
                        elif choice2 == 'n':

                            break

                        else:

                            print("Invaild Argument")

                        sleep(2) 
                    
                    case 3:

                        print("Selected Food")

                        print("How many you want to buy")

                        no_of_food = int(input("> "))

                        print(no_of_food)

                        sleep(2)

                        print(f"Are you sure you want to buy {no_of_food} Food")

                        choice2 = str(input("> "))

                        if choice2 == 'y':

                            print("okay")

                            player_money = player_money - (no_of_food * food)

                            if player_money < 0:

                                print("You cannot buy these many Food")
                                
                                sleep(4)
                                
                                player_money = player_money + (no_of_food * food)

                            else:

                                print("You are good to go")

                                sleep(2)
                                
                        elif choice2 == 'n':

                            break

                        else:

                            print("Invaild Argument")

                        sleep(2)
                    
                    case 4:

                        print("Selected Jewellery")

                        print("How many you want to buy")

                        no_of_food = int(input("> "))

                        print(no_of_food)

                        sleep(2)

                        print(f"Are you sure you want to buy {no_of_food} Jewellery")

                        choice2 = str(input("> "))

                        if choice2 == 'y':

                            print("okay")

                            player_money = player_money - (no_of_food * jew)

                            if player_money < 0:

                                print("You cannot buy these many Jewellery")
                                
                                sleep(4)
                                
                                player_money = player_money + (no_of_food * jew)

                            else:

                                print("You are good to go")

                                sleep(2)
                                
                        elif choice2 == 'n':

                            break

                        else:

                            print("Invaild Argument")

                        sleep(2)
                    
                    case 5:

                        print("Selected Cannons")

                        print("How many you want to buy")

                        no_of_food = int(input("> "))

                        print(no_of_food)

                        sleep(2)

                        print(f"Are you sure you want to buy {no_of_food} Cannons")

                        choice2 = str(input("> "))

                        if choice2 == 'y':

                            print("okay")

                            player_money = player_money - (no_of_food * cannons)

                            if player_money < 0:

                                print("You cannot buy these many Cannons")
                                
                                sleep(4)
                                
                                player_money = player_money + (no_of_food * cannons)

                            else:

                                print("You are good to go")

                                sleep(2)
                                
                        elif choice2 == 'n':

                            break

                        else:

                            print("Invaild Argument")

                        sleep(2)
                    
                    case 6:

                        print("Cannon balls")

                        print("How many you want to buy")

                        no_of_food = int(input("> "))

                        print(no_of_food)

                        sleep(2)

                        print(f"Are you sure you want to buy {no_of_food} Cannon balls")

                        choice2 = str(input("> "))

                        if choice2 == 'y':

                            print("okay")

                            player_money = player_money - (no_of_food * cannon_balls)

                            if player_money < 0:

                                print("You cannot buy these many Cannon balls")
                                
                                sleep(4)
                                
                                player_money = player_money + (no_of_food * cannon_balls)

                            else:

                                print("You are good to go")

                                sleep(2)
                                
                        elif choice2 == 'n':

                            break

                        else:

                            print("Invaild Argument")

                        sleep(2)
            
            elif choice == 'a':

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

            minigame()

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
