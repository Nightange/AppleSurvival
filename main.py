import characters as c
import aid_functions as f
import os 
import time

#intro function to make the user and enemy
def intro():
    time.sleep(1)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    print("Welcome to my game! \n You are an apple, in a world full of hungry dragons. You must survive. ")
    name = input("What would you like to name your apple? ")
    if "mina" in name.lower():
        print("Sam loves you! ")
    print("Hello", name)
    while True:
        difficulty = input("Would you like to play on easy, medium, or hard? ").lower()
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            break
        print("Please choose easy, medium, or hard")


    difficulty_map = {
        "easy": {"health": 100, "damage": 20},
        "medium": {"health": 200, "damage": 35},
        "hard" : {"health": 350, "damage": 50},
    }
    dragon = c.dragon(**difficulty_map[difficulty])
    user = c.apple(name, 100, 50, 3, 0)
    return user, dragon 

#function to print the world map and get where user wants to go
def world_map():
    print("This is the map of the area: ")
    print("1. Home 2. Neighbors Home 3. Cemetery ")
    print("4. Orchard 5. Lake 6. Hospital ")
    print("7. Fruit Store 8. Forest 9. Cave ")
    location = f.get_number("Where would you like to go?(number) ")
    return location

#main game function, loops until user loses or wins
def main_game(user, dragon):
    while True:
        time.sleep(1)
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        print("Welcome to Appleland,", user.name, "\b! An evil dragon has invaded! Find food to stay alive; let the dragon get you too many times: you die!")
        key = world_map()
        movement = {
            1: f.home,
            2: f.n_home,
            3: f.cemetery,
            4: f.orchard, 
            5: f.lake,
            6: f.hospital,
            7: f.store,
            8: f.forest,
            9: f.cave,
        }
        movement[key](user, dragon)

#main function, runs the game in order
def main():
    user, dragon = intro()
    main_game(user, dragon)

#makes sure this is the main file
if __name__ == "__main__":
    main()