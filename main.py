import characters as c

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

def main_game():
    pass
    

def main():
    intro()
    main_game()

if __name__ == "__main__":
    main()