import aid_functions as f
import random as r

#main character, the user
class apple:
    #initializing function
    def __init__(self, name, health, hunger, turns, total_turns):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.turns = turns
        self.total_turns = total_turns
        self.weapon_name = None
        self.weapon_damage = 0
    
    #function to change the health, up, down from hunger, down from dragon, and kill
    def health_changer(self, a, dragon):
        if a == "u":
            if self.health < 100:
                self.health += 10
            else:
                print("You're at max health!\n")
        elif a == "h":
            self.health -= 10
            if self.health <= 0:
                f.lose(self, dragon)
        elif a == "d":
            self.health -= dragon.damage
            if self.health <= 0:
                f.lose(self, dragon)
            dragon.health_changer(self, "d")
            if self.weapon_damage != 0:
                print("Your weapon broke! ")
                self.weapon_damage = 0
                self.weapon_name = None
        elif a == "k":
            f.lose(self, dragon)

    #function to change hunger down or up
    def hunger_changer(self, a):
        if a == "d":
            self.hunger -= 10
            if self.hunger == 0:
                self.health_changer("h")
        elif a == "u":
            if self.hunger >= 50:
                print("You're full.")
            else:
                self.hunger += 10
    
    #function to give the character a weapon
    def weapon_maker(self, loco):
        chance = r.randint(0, 100)
        for i in range(len(loco)):
            if i%3 == 0:
                if chance <= loco[i]:
                    self.weapon_name = loco[i+1]
                    self.weapon_damage = loco[i+2]
                    if self.weapon_name == "suture kit":
                        print("You found a",self.weapon_name,"which heals 20 hp!")
                        self.health_changer("u", None)
                        self.health_changer("u", None)
                        self.weapon_name = None
                    else:
                        print("You found a",self.weapon_name,"which does",self.weapon_damage,"damage!")
                    return
        print("You found nothing.")
        
    #function to attack when encountering dragon
    def attack(self):
        if self.weapon_name != None:
            print("You attack! ")
        return self.weapon_damage

#character for the enemy
class dragon:
    #initializing function
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage
    
    #health changer for dragon, changing when attacked
    def health_changer(self, user, a):
        if a == "d":
            self.health -= user.attack()
            print(self.health)
            if self.health == 0:
                f.win(user, self)