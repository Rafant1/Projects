import random
from pprint import pprint


class Hero():
    def __init__(self, Hname, Hhealth, Hattack_points, Hdefense_points, Hrange_attack_points, Hmagic_attack_points, Hluck, Halive = True):
        self.name = Hname
        self.health = Hhealth
        self.attack_points = Hattack_points
        self.defense_points = Hdefense_points
        self.range_attack_points = Hrange_attack_points
        self.magic_attack_points = Hmagic_attack_points
        self.luck = Hluck
        self.alive = Halive

    def get_health(self):
        return self.health
    def get_attack(self):
        return self.attack_points
    def get_defense(self):
        return self.defense_points
    def get_range_attack(self):
        return self.range_attack_points
    def get_magic_attack(self):
        return self.magic_attack_points
    def get_luck(self):
        return self.luck
    def get_alive(self):
        return self.alive

    def set_health(self, new_health):
        self.health = new_health
    def set_attack(self, new_attack):
        self.attack_points = new_attack
    def set_defense(self, new_defense):
        self.defense_points = new_defense
    def set_range_attack(self, new_range):
        self.range_attack_points = new_range
    def set_magic_attack(self, new_magic):
        self.magic_attack_points = new_magic
    def set_alive(self, new_alive):
        self.alive = new_alive


def create_your_class():
#From this function the class Hero will take the main arguments

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
        range_attack_points = 4
        magic_attack_points = 2
        hero_class = "Warrior"
        hero_alive = True
    elif a == "2":
        health = 125
        attack_points = 6
        defense_points = 10
        range_attack_points = 2
        magic_attack_points = 1
        hero_class = "Knight"

    elif a == "3":
        health = 75
        attack_points = 4
        defense_points = 4
        range_attack_points = 8
        magic_attack_points = 2
        hero_class = "Archer"

    elif a == "4":
        health = 50
        attack_points = 3
        defense_points = 2
        range_attack_points = 4
        magic_attack_points = 10
        hero_class = "Mage"

    else:
        print("You didn't chose any class. Try again.")

    input("\nPress enter to roll a dice in order to check what is your luck value.")
    luck = random.randint(0, 10)
    print(f"Your hero has {luck} point(s) of luck out of 10.")
    return name, health, attack_points, defense_points, range_attack_points, magic_attack_points, luck, hero_class,




Hero_attributes = create_your_class()
Hero1 = Hero(Hero_attributes[0], Hero_attributes[1], Hero_attributes[2], Hero_attributes[3], Hero_attributes[4], Hero_attributes[5], Hero_attributes[6])
print(f"The class you selected is {Hero_attributes[7]}. Those are your attributes:")
print(f"name: {Hero1.name}")
print(f"health: {Hero1.health}")
print(f"attack points: {Hero1.attack_points}")
print(f"defense points: {Hero1.defense_points}")
print(f"range attack points: {Hero1.range_attack_points}")
print(f"magic attack points: {Hero1.magic_attack_points}")
print(f"points of luck: {Hero1.luck}")
print(Hero1.alive)








class Enemy():
    #Etype = enemy type(based on True or False of this parameter, the enemy will be regular or will become a boss)
    def __init__(self, Ename, Etype, Ehealth, Especial_attack_points, Eattack_points, Edefense_points, Enormal_attack_vulnability, Erange_attack_vulnability, Emagic_attack_vulnability, Ealive = True):
        self.name = Ename
        self.type = Etype
        self.health = Ehealth
        self.special_attack_points = Especial_attack_points
        self.attack_points = Eattack_points
        self.defense_points = Edefense_points
        self.normal_attack_vulnability = Enormal_attack_vulnability
        self.range_attack_vulnability = Erange_attack_vulnability
        self.magic_attack_vulnability = Emagic_attack_vulnability
        self.alive = Ealive

    def get_health(self):
        return self.health
    def get_special_attack(self):
        return self.special_attack_points
    def get_attack(self):
        return self.attack_points
    def get_defense(self):
        return self.defense_points
    def get_normal_attack_vulnability(self):
        return self.normal_attack_vulnability
    def get_range_attack_vulnability(self):
        return self.range_attack_vulnability
    def get_magic_attack_vulnability(self):
        return self.magic_attack_vulnability
    def get_alive(self):
        return self.alive


    def set_health(self, new_health):
        self.health = new_health
    def set_attack(self, new_attack):
        self.attack_points = new_attack
    def set_defense(self, new_defense):
        self.defense_points = new_defense
    def set_special(self, new_special):
        self.special_attack_points = new_special
    def set_normal_attack_vulnability(self, new_attack_vulnability):
        self.normal_attack_vulnability = new_attack_vulnability
    def set_range_attack_vulnability(self, new_range_vulnability):
        self.range_attack_points = new_range_vulnability
    def set_magic_attack_vulnability(self, new_magic_attack_vulnability):
        self.range_attack_points = new_magic_attack_vulnability
    def set_alive(self, new_alive):
        self.alive = new_alive








def enemy_name_generator():
    file = open("Adjective.txt", "r")
    lines = file.readlines()
    adjective = lines[random.randint(0, len(lines)-1)][:-1]
    file.close
    file = open("Creature.txt", "r")
    lines = file.readlines()
    creature = lines[random.randint(0, len(lines)-1)][:-1]
    file.close
    creature_name = adjective + " " + creature
    return creature_name

def enemy_values_generator():
    #numbers_to_draw will choose a random number from 1 to 10 and based on that will set the enemy type and its random parameters. Numbers from 9 to 10 will generate boss enemy type.
    numbers_to_draw = [1,2,3,4,5,6,7,8,9,10]
    drawn_number = random.choice(numbers_to_draw)
    if drawn_number == 9 and drawn_number == 10:
        enemy_type = "boss"
        health = random.randint(30,50)
        special_attack_points = random.randint(20,30)
        attack_points = random.randint(10,20)
        defense_points =  random.randint(5,10)
        normal_attack_vulnability = random.randint(0,4)
        range_attack_vulnability = random.randint(0,4)
        magic_attack_vulnability = random.randint(0,4)
    else:
        enemy_type = "normal"
        health = random.randint(10, 30)
        special_attack_points = random.randint(10, 20)
        attack_points = random.randint(1,10)
        defense_points = random.randint(0,5)
        normal_attack_vulnability = random.randint(0, 8)
        range_attack_vulnability = random.randint(0, 8)
        magic_attack_vulnability = random.randint(0, 8)

    return enemy_type, health, special_attack_points, attack_points, defense_points, normal_attack_vulnability, range_attack_vulnability, magic_attack_vulnability


enemy_name = enemy_name_generator()
enemy_values = enemy_values_generator()
en1 = Enemy(enemy_name,enemy_values[0],enemy_values[1],enemy_values[2],enemy_values[3],enemy_values[4],enemy_values[5],enemy_values[6], enemy_values[7])
pprint(vars(en1))










def enemy_dead(enemy):
    if enemy.get_health() <= 0:
        print("Congratulations! You defeated the monster!")
        enemy.set_alive(False)



def enemy_attack(hero, enemy):
    enemy_attack_multiplicator = random.randint(1,3)
    chance_attack = random.randint(1,10)
    if chance_attack >= 6:
        hero.set_health(hero.get_health() - (enemy.get_attack() * enemy_attack_multiplicator))
        print("It is the enemy turn...")
        print(f"The enemy dealt you {enemy.get_attack() + enemy_attack_multiplicator} damage points.")
        print(f"Your actual health is {hero.get_health()} health points.\n")
    else:
        print("The enemy tried to hit you, but it missed.")
        print(f"Your actual health is {hero.get_health()} health points.\n")



def player_attack(hero, enemy):
    player_attack_type = input('''What type of attack would you like to chose?
1. normal attack
2. ranged attack
3. magic attack
''')
    if player_attack_type == "1":
        chance_attack = random.randint(1, 10)
        if chance_attack >= 6:
            enemy.set_health(enemy.get_health() - hero.get_attack() - enemy.get_normal_attack_vulnability())
            print("You swing the sword...")
            print(f"You dealt {hero.get_attack() + enemy.get_normal_attack_vulnability()} damage points.")
            print(f"The actual enemy health is {enemy.get_health()}.\n")


        else:
            print("You swing the sword...")
            print("Unfortunately, you missed.")
            print(f"The actual enemy health is {enemy.get_health()}.\n")






def battle(hero, enemy):
    while enemy.get_alive() == True:
        player_attack(hero,enemy)
        enemy_dead(enemy)
        if enemy.get_alive() == False:
            break
        enemy_attack(hero,enemy)




battle(Hero1, en1)
print("The enemy is dead.")