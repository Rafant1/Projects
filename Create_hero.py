import random
from pprint import pprint


class Hero():
    def __init__(self, Hname, Hhealth, Hattack_points, Hdefense_points, Hrange_attack_points, Hmagic_attack_points, Hluck):
        self.name = Hname
        self.health = Hhealth
        self.attack_points = Hattack_points
        self.defense_points = Hdefense_points
        self.range_attack_points = Hrange_attack_points
        self.magic_attack_points = Hmagic_attack_points
        self.luck = Hluck

    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack_points
    def getDefense(self):
        return self.defense_points
    def getRangeAttack(self):
        return self.range_attack_points
    def getMagicAttack(self):
        return self.magic_attack_points
    def getLuck(self):
        return self.luck


    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack_points = newAttack
    def setDefense(self, newDefense):
        self.defense_points = newDefense
    def setRangeAttack(self, newRange):
        self.range_attack_points = newRange
    def setMagicAttack(self, newMagic):
        self.magic_attack_points = newMagic


def Create_your_class():

    name = input("What name you would like to chose? ")
    print(f"Hello, {name}.")

    a = None


    while a != "1" and a != "2" and a != "3" and a != "4":
        a = input('''
Which class would you like to chose?
Warrior(1)
Knight(2)
Archer(3)
Mage(4)
''')

    if a == "1":
        health = 100
        attack_points = 10
        defense_points = 6
        range_attack_points = 2
        magic_attack_points = 0
        hero_class = "Warrior"
    elif a == "2":
        health = 125
        attack_points = 6
        defense_points = 10
        range_attack_points = 2
        magic_attack_points = 0
        hero_class = "Knight"
    elif a == "3":
        health = 75
        attack_points = 4
        defense_points = 4
        range_attack_points = 8
        magic_attack_points = 0
        hero_class = "Archer"
    elif a == "4":
        health = 50
        attack_points = 2
        defense_points = 2
        range_attack_points = 1
        magic_attack_points = 10
        hero_class = "Mage"
    else:
        print("You didn't chose any class. Try again.")

    input("\nPress enter to roll a dice in order to check what is your luck value.")
    luck = random.randint(0, 10)
    print(f"Your hero has {luck} point(s) of luck out of 10.")
    return name, health, attack_points, defense_points, range_attack_points, magic_attack_points, luck, hero_class




Hero_attributes = Create_your_class()
Hero1 = Hero(Hero_attributes[0], Hero_attributes[1], Hero_attributes[2], Hero_attributes[3], Hero_attributes[4], Hero_attributes[5], Hero_attributes[6])
print(f"The class you selected is {Hero_attributes[7]}. Those are your attributes:")
print(f"name: {Hero1.name}")
print(f"health: {Hero1.health}")
print(f"attack points: {Hero1.attack_points}")
print(f"defense points: {Hero1.defense_points}")
print(f"range attack points: {Hero1.range_attack_points}")
print(f"magic attack points: {Hero1.magic_attack_points}")
print(f"points of luck: {Hero1.luck}")