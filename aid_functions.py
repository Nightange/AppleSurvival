import random as r
import characters as c
from main import main
import os
import time

#function to filter map input
def get_number(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num < 1 or num > 9:
                print("\nThat isn't a place on the map, try again!\n")
            else:
                return num
        except ValueError:
            print("\nThat isn't a place on the map, try again! \n")

#function to print the user and dragon info
def get_info(user, dragon):
    print("\nApple Name:",user.name)
    print("Health:",user.health)
    print("Hunger:",user.hunger)
    print("Weapon:",user.weapon_name)
    print("Armor:",user.armor_name)
    print("\nDragon Health:",dragon.health)
            
#function for the chance to get food            
def food_chance(user, odds):
    chance = r.randint(1,10)
    if chance >= odds:
        print("\nYou found food! ")
        user.hunger_changer("u", None)
    
    return chance

#function for the chance of a dragon encounter
def dragon_chance(user, dragon):
    chance = r.randint(1,10)
    if chance >= 8:
        print("\nThe dragon attacks! ")
        user.health_changer("d", dragon)

#turn count, the longer a player does stuff somewhere, the higher risk of a dragon encounter        
def turn_count(user, dragon):
    turns = user.turns
    if turns > 0:
        user.turns -= 1
        user.total_turns += 1
    else:
        dragon_chance(user, dragon)
        user.turns = 3
        time.sleep(.5)
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
#home location
def home(user, dragon):
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        print("Welcome to your home! ")
        print("You can: 1. Look for food 2. Sleep 3. Leave")
        get_info(user, dragon)
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You look for food.")
            turn_count(user, dragon)
            food_chance(user, 8)
        elif action == "2":
            print("You sleep.")
            turn_count(user, dragon)
            user.health_changer("u", dragon)
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")
        
#neighbors home location
def n_home(user, dragon):
    n_home_weapons = [5, "gun", 50, 10, "knife", 20, 20, "broom", 10]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        print("Welcome to your neighbors house! It seems he isn't home. ")
        print("You can: 1. Look for food 2. Snoop 3. Leave")
        get_info(user, dragon)
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You look for food.")
            turn_count(user, dragon)
            food_chance(user, 8)
        elif action == "2":
            print("You snoop around his house.")
            user.weapon_maker(n_home_weapons)
            turn_count(user, dragon)
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")

#cemetery location
def cemetery(user, dragon):
    cemetery_weapons = [10, "ghostly sword", 30, 15, "pipe", 20, 30, "cross", 10]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the Appleland Cemetery! The air is eerily still; even the birds are quiet.")
        print("You can: 1. Walk 2. Mourn 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You walk around.")
            turn_count(user, dragon)
        elif action == "2":
            print("You mourn your fallen friends.")
            turn_count(user, dragon)
            user.weapon_maker(cemetery_weapons)
            user.item_lister("Ghost of Appleland's Founder")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")

#orchard location
def orchard(user, dragon):
    orchard_armor = [10, "wood armor", 10, 15, "fruit armor", 5, 25, "grass armor", 2]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the Appleland Orchard! This is where all the fruit you eat is grown. ")
        print("You can: 1. Search the area 2. Climb a tree 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You search the area.")
            turn_count(user, dragon)
            user.armor_maker(orchard_armor)
        elif action == "2":
            print("You climb a tree.")
            turn_count(user, dragon)
            dragon_chance(user, dragon)
            user.item_lister("Dragon Egg")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")
                
#lake location
def lake(user, dragon):
    lake_armor = [10, "coral armor", 10, 15, "ice armor", 5, 25, "water armor", 2]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the lake! The water seems to be buzzing with energy. ")
        print("You can: 1. Walk along the shore 2. Go for a swim 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You go for a stroll.")
            turn_count(user, dragon)
            user.armor_maker(lake_armor)
        elif action == "2":
            print("You go for a swim.")
            turn_count(user, dragon)
            dragon_chance(user, dragon)
            user.item_lister("Aquamarine Pendant")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")
                
#hospital location
def hospital(user, dragon):
    hospital_weapons = [10, "gurney", 30, 20, "suture kit", 0, 30, "scalpel", 10]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the Appleland Hospital! Weak and sick apples would congregate here, before the dragon attacked. ")
        print("You can: 1. Look for food 2. Search for medical supplies 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You look for food.")
            turn_count(user, dragon)
            food_chance(user, 10)
        elif action == "2":
            print("You look for supplies.")
            turn_count(user, dragon)
            user.weapon_maker(hospital_weapons)
            user.item_lister("Doctors License")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")

#store location
def store(user, dragon):
    store_weapons = [10, "machete", 30, 10, "axe", 30, 30, "mop", 10]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the Appleland Store! All the orchard's ripe fruits come here. ")
        print("You can: 1. Look for food 2. Look for a weapon 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You look for food.")
            turn_count(user, dragon)
            food_chance(user, 6)
        elif action == "2":
            print("You look for a weapon.")
            turn_count(user, dragon)
            user.weapon_maker(store_weapons)
            user.item_lister("Gold Bar")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")
    
#forest location
def forest(user, dragon):
    forest_armor = [10, "thorny armor", 10, 15, "fur armor", 5, 25, "leaf armor", 2]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the forest! You seem to be far from home, tread carefully. ")
        print("You can: 1. Look around 2. Go deeper 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You look around the trees.")
            turn_count(user, dragon)
            user.armor_maker(forest_armor)
        elif action == "2":
            print("You go deeper into the forest.")
            turn_count(user, dragon)
            dragon_chance(user, dragon)
            user.item_lister("Animal Bone")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")

#cave location
def cave(user, dragon):
    cave_armor = [1, "dragon scale armor", 15, 10, "stone armor", 10, 15, "bone armor", 5]
    user.turns = 3
    food_chance(user, 10)
    dragon_chance(user, dragon)
    user.hunger_changer("d", dragon)
    while True:
        get_info(user, dragon)
        print("Welcome to the cave! This is the dragon's den, it'd be wise to leave quickly. ")
        print("You can: 1. Look around 2. Explore 3. Leave")
        action = input("What would you like to do?(number) ")
        if action == "1":
            print("You look around the evil cave.")
            turn_count(user, dragon)
            user.armor_maker(cave_armor)
            dragon_chance(user, dragon)
        elif action == "2":
            print("You explore the cave.")
            turn_count(user, dragon)
            dragon_chance(user, dragon)
            user.item_lister("Dragon's Jewels")
        elif action == "3":
            print("You leave.")
            return
        else:
            print("Please put in a number")
    
#function to save the score
def save_score(user, a):
    print("You survived for",user.total_turns,"turns")
    with open('scores.txt', 'a') as f:
        user.total_turns += 100 * len(user.items)
        f.write(user.name)
        f.write(":")
        if a == "w":
            user.total_turns += 100
            f.write(str(user.total_turns))
            f.write(" Won ")
            f.write(user.difficulty)
            f.write("\n")
            if len(user.items) == 7:
                print("You found all the secret items and got the best ending! Appleland will prosper!")
            else:
                print("You won, but you didn't find all the secret items. Appleland will never be the same.")
        else:
            f.write(str(user.total_turns))
            f.write(" Lost ")
            f.write(user.difficulty)
            f.write("\n")
            print("You died. Appleland is in ruins.")

#function to play again
def restart(user, dragon, a):
    while True:
        save = input("Would you like to save your score?(y/n) ")
        if save.lower() == "n":
            break
        if save.lower() == "y":
            save_score(user, a)
            break
        else:
            print("Please put y or n.")
    while True:
        rerun = input("Would you like to play again? (y/n) ")
        if rerun.lower() == "n":
            del user
            del dragon
            exit()
        elif rerun.lower() == "y":
            del user
            del dragon
            main()
        else:
            print("Please put y or n. ")
            
#lose function
def lose(user, dragon):
    print("You lose! ")
    restart(user, dragon, "l")
    
#win function
def win(user, dragon):
    print("You have killed the dragon and saved Appleland! ")
    print("You win! ")
    restart(user, dragon, "w")