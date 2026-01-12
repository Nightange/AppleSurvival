import characters as c
import aid_functions as f
import os 
import time

def intro():
    print("Welcome to my game! \n You are an apple, in a world full of hungry dragons. You must survive. ")
    name = input("What would you like to name your apple? ")
    if name.lower() == "mina":
        print("Sam loves you! ")
    print("Hello", name)
    while True:
        difficulty = input("Would you like to play on easy, medium, or hard? ").lower()
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            break
        print("Please choose easy, medium, or hard")
    
    
    difficulty_map = {
        "easy": {"health": 50, "damage": 20},
        "medium": {"health": 100, "damage": 35},
        "hard" : {"health": 200, "damage": 50},
    }
    dragon = c.dragon(**difficulty_map[difficulty])
    user = c.apple(name, 100, 50)
    time.sleep(1)
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
    return user, dragon 

def world_map():
    print("This is the map: ")
    print("1. Home 2. x 3. x ")
    print("4. x 5. x 6. x ")
    print("7. x 8. x 9. x ")
    location = f.get_number("Where would you like to go? ")

def main_game(user, dragon):
    print("Welcome to Appleland,", user.name, "\b! Dragons have invaded! Find food to stay alive; let the dragons get you too many times: you die!")
    
    

def main():
    user, dragon = intro()
    main_game(user, dragon)

if __name__ == "__main__":
    main()