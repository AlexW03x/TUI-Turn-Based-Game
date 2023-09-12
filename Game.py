import random
import sys
import math
import os
import string

from Enemy_Creation import Enemy
from Player_Creation import Player

global p

def clear():
    for i in range(0,99):
        print("\n")

def save_game(x):
    f = open(os.path.join(os.getcwd(), "data.txt"), "w")
    for item in x:
        f.write(str(item) + "\n")

def main():
    print("Welcome to AlexW03x Turn-Based Game!")
    print("=======================================")
    print("=                        1. Play Game                      =")
    print("=                        2. Exit Game                      =")
    print("=======================================")

    while True:
        try:
            a = int(input("Option: "))
            if a == 1:
                game()
            if a == 2:
                sys.exit(0)
            break
        except ValueError:
            continue
        except TypeError:
            continue
                   
def game_p2():
    global variables
    global p
    p = Player(variables[0], variables[1], variables[2], variables[3], variables[4], variables[5], variables[6])
    clear()
    print("You are on level: " + str(variables[6]))
    names = ["Alex", "Ben", "Chris", "Charlie", "Divine", "Devonte", "Dax", "Ethan", "Eman", "Evan", "Folly", "Felix", "Finn", "Gant", "Gin", "Giola", "Harry", "Himothy", "Harold", "Isaac", "Izu", "Irakli", "Jimmy", "Joe", "Jake", "Kaz", "Keiran", "Kasper", "Lucas", "Luke", "Liam", "Mike", "Max", "Miro", "Nathan", "Neil", "Noah", "Owen", "Oliver", "Omar", "Preston", "Parker", "Patrick", "Quinn", "Quentin", "Qamar", "Ron", "Rowan", "Ryan", "Sam", "Seb", "Spencer", "Tom", "Timothy", "Tyler", "Ulysses", "Umar", "Usher", "Victor", "Vance", "Vale", "Will", "Walter", "Wyatt", "Xavier", "Xerxes", "Xander", "Yoshi", "Yusuf", "Yakov", "Zach", "Zion", "Zander"]
    etype = ["Blademaster", "Pyromancer", "Cryomancer", "Soldier", "Boxer", "Necromancer", "Paladin", "Samurai", "Corrupted", "Fatebringer", "Commander", "Lieutenant", "Assassin", "Chaos Bringer", "Viking", "Oppressor", "Tyrant", "Knight", "Villain", "Werewolf", "Zombie", "Mutant", "Legend", "Unpleased", "Drained"]

    ename = random.choice(names)
    ety = random.choice(etype)
    enemy = Enemy(ename, round(200 * (1 + (int(p.level)/10)), 0), round(75 * (1 + (int(p.level)/5)), 0), round(10 * (1 + (int(p.level)/10)), 0), round(2 * (1 + (int(p.level)/10)),0), ["Basic Attack", "Special Attack"])
    while True:#
        clear()
        print("You've come across: " + ename + " The " + ety)
        print("Would you like to?")
        print("1. Battle the enemy?")
        print("2. Reveal info about enemy?")
        print("3. Exit to menu?")

        try:
            opt = int(input("Option: "))
            if opt == 1:
                break
            if opt == 2:
                print(ename + " The " + ety + " Info:")
                print("HP: " + str(enemy.hp))
                print("MP: " + str(enemy.mp))
                print("Power: " + str(enemy.power))
                print("Speed: "+ str(enemy.speed))
                print("1. Return to options?")
                o = input("[type anything]...")
                continue
            if opt == 3:
                main()
                break
        except ValueError:
            continue
        except TypeError:
            continue

    ##battle phase##
    turn = "self"
    clear()
    while True:#
        print("\n")
        if int(enemy.hp) <= 0:
            print("Enemy defeated!")
            p.modify("level", int(p.level) + 1)
            print("Proceed to next level?")
            print("1. Yes")
            print("2. Return to menu")
            listed = []
            listed.append(p.name)
            listed.append(p.max_hp)
            listed.append(p.max_mp)
            listed.append(p.power)
            listed.append(p.speed)
            listed.append(p.class_type)
            listed.append(p.level)

            save_game(listed)
            try:
                f = open('data.txt', "r")
                for items in f:
                    variables.append(items.strip()) ##fix variables
                f.close()
            except FileNotFoundError:
                    f = open(os.path.join(os.getcwd(), "data.txt"), "w")
                    for item in x:
                        f.write(str(item) + "\n")
                    save_game(listed)

                    f = open('data.txt', "r")
                    for items in f:
                        variables.append(items.strip()) ##fix variables
                    f.close()
            try:
                axs = int(input("Option: "))
                if axs == 1:
                    game_p2()
                if axs == 2:
                    main()
            except ValueError:
                continue
            except TypeError:
                continue
            break

        if int(p.hp) <= 0:
            print("You've lost the battle!")
            print("1. Find new opponent")
            print("2. Return to Menu")
            try:
                axs = int(input("Option: "))
                if axs == 1:
                    game_p2()
                if axs == 2:
                    main()
            except ValueError:
                continue
            except TypeError:
                continue
            break
            
        if turn == "self" and int(p.hp) > 0 and int(enemy.hp) > 0: ##you always attack first before enemy does##
            print("Its your turn to attack!")
            print("You have " + str(p.hp) + "HP and " + str(p.mp) + "MP!")
            print("1. Basic Attack [0MP]")
            print("2. Special Attack [25MP]")
            print("3. Heal [40MP]")

            try:
                atk = int(input("Option: "))
                if atk == 1:
                    misschance = random.randint(0,100)
                    if round(int(p.speed), 0 ) < misschance:
                        dmg = round(int(p.power) * 2,0)
                        print("You dealt " + str(dmg) + " dmg with basic attack!")

                        enewhp = int(enemy.hp) - dmg
                        managained = round(int(p.max_mp)/5,0)
                        selfnewmp = int(p.mp) + round(int(p.max_mp) / 5, 0)
                        if(enewhp <= 0):
                            print("Enemy defeated!")
                            enemy.modify("hp", 0)
                        else:
                            enemy.modify("hp", enewhp)
                            if(selfnewmp >= int(p.max_mp)):
                                p.modify("mp", int(p.max_mp))
                            else:
                                p.modify("mp", int(selfnewmp))
                            print("Enemy is now on: " + str(enemy.hp) + "HP!")
                            print("You've gained: " + str(managained) + "MP!")

                    else:
                        print("You've missed!")
                    turn = "enemy"
                if atk == 2:
                    misschance = random.randint(0,100)
                    if(int(p.mp) >= 25):
                        if round(int(p.speed), 0 ) <= misschance:
                            dmg = round(int(p.power) * 3,0)
                            print("You dealt " + str(dmg) + " dmg with special attack!")

                            enewhp = int(enemy.hp) - dmg
                            if(enewhp <= 0):
                                print("Enemy defeated!")
                                enemy.modify("hp", 0)
                            else:
                                enemy.modify("hp", enewhp)
                                print("Enemy is now on: "+ str(enemy.hp) + "HP!")
                                print("You've used: 25 MP!")

                            p.modify("mp", int(p.mp) - 25)

                        else:
                            print("You've missed!")
                        turn = "enemy"
                    else:
                        print("Not enough MP!")
                        
                    
                if atk == 3:
                    if(int(p.mp) >= 40):
                        health_to_gain = round(int(p.mp),0)
                        print("You used heal to gain: " + str(health_to_gain) + "HP!")
                        new_health = int(p.hp) + health_to_gain
                        if (new_health >= int(p.max_hp)):
                            p.modify("hp", int(p.max_hp))
                        else:
                            p.modify("hp", int(new_health))

                        p.modify("mp", int(p.mp) -40)
                        print("Your HP: " + str(p.hp))
                        print("Your MP: " + str(p.mp))

                        turn = "enemy"
                    else:
                        print("Not enough MP!")

            except ValueError:
                continue
            except TypeError:
                continue

        if turn == "enemy" and int(p.hp) > 0 and int(enemy.hp) > 0:
            print("\n")
            opt = random.randint(0,2)
            if opt == 1 or opt == 0: #dmg player
                misschance = random.randint(0,100)
                if round(int(p.speed)) <= misschance:
                    dmg = round(int(enemy.power) * 1.5, 0)
                    print("Enemy dealt " + str(dmg) + " dmg with basic attack!")

                    selfnewhp = int(p.hp) - dmg
                    managained = round(int(enemy.max_mp)/5, 0)
                    enemynewmp = int(enemy.mp) + managained
                    if(selfnewhp <= 0):
                        print("Enemy defeated you!")
                        p.modify("hp", 0)
                    else:
                        p.modify("hp", selfnewhp)
                        if(enemynewmp >= int(enemy.max_mp)):
                            enemy.modify("mp", int(enemy.max_mp))
                        else:
                            enemy.modify("mp", int(enemynewmp))

                        print("You are now on: " + str(p.hp) + "HP!")
                        print("Enemy now has: " + str(enemy.mp) + "MP!")
                else:
                    print("Enemy Missed Attack!")

            if opt == 2: #special attack
                misschance = random.randint(0,100)
                if(int(enemy.mp) >= 25):
                    if round(int(p.speed)) <= misschance:
                        dmg = round(int(enemy.power) * 2, 0)
                        print("Enemy dealt " + str(dmg) + " dmg with special attack!")

                        selfnewhp = int(p.hp) - dmg
                        enemynewmp = int(enemy.mp) - 25
                        if(selfnewhp <= 0):
                            print("Enemy defeated you!")
                            p.modify("hp", 0)
                        else:
                            p.modify("hp", selfnewhp)

                        enemy.modify("mp", enemynewmp)
                        print("You are now on: " + str(p.hp) + "HP!")
                        print("Enemy now has: " + str(enemy.mp) + "MP!")
                    else:
                        print("Enemy Missed Special Attack!")
                else:
                    continue

            if opt == 0 or opt == 1 or opt == 2:
                turn = "self"
                continue
                

global variables
def game():
    global variables
    variables = []
    clear()
    ##check for save game##
    try:
        f = open('data.txt', "r")
        for items in f:
            variables.append(items.strip()) ##fix variables
        f.close()
        print("Save game detected! Would you like to...")
        print("1. Play from save")
        print("2. Create new save")
        while True:
            try:
                ops = int(input("Option: "))
                if ops == 1:
                    game_p2()
                if ops == 2:
                    createnew()
                break
            except TypeError:
                continue
            except ValueError:
                continue
    except FileNotFoundError:
        print("Save not detected... Creating new save!")
        createnew()

def createnew():
    print("=====================================")
    while True:
            name = str(input("Character Name: "))
            if len(name) == 0:
                continue
            else:
                break

    print("=====================================")
    print("=                    Select a Class                   =")
    print("=====================================")
    print("=                       1. Warrior                        =")
    print("=                         2. Mage                         =")
    print("=                     3. Assassin                       =")
    print("=                       4. Hybrid                         =")
    print("=====================================")

    while True:
        try:
            classe = int(input("Option: "))
            if classe < 5:
                break
            else:
                continue
        except ValueError:
            continue
        except TypeError:
            continue

    classe = "Warrior" if classe == 1 else "Mage" if classe == 2 else "Assassin" if classe == 3 else "Hybrid"
    print("You selected: " + classe)
    print("=====================================")
    global p
    if classe == "Warrior":
        p = Player(name, 200, 50, 15, 3, "Warrior", 1)
    elif classe == "Mage":
        p = Player(name, 250, 100, 7, 5, "Mage", 1)
    elif classe == "Assassin":
        p = Player(name, 120, 70, 10, 15, "Assassin",  1)
    else:
        p = Player(name, 165, 70, 11, 8, "Hybrid", 1)


    print("1. Save Character Choice?")
    print("2. Reselect Character?")
    print("3. Exit To Menu")

    while True:
        try:
            opt = int(input("Option: "))
            if opt == 1:
                listed = []
                listed.append(p.name)
                listed.append(p.hp)
                listed.append(p.mp)
                listed.append(p.power)
                listed.append(p.speed)
                listed.append(p.class_type)
                listed.append(p.level)

                save_game(listed)
                game_p2()
            if opt == 2:
                clear()
                return createnew()
            if opt == 3:
                clear()
                return main()
            break
        except ValueError:
            continue
        except TypeError:
            continue
    
        
    
    
    

main()
