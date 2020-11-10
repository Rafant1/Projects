import random
from pprint import pprint

class Enemy():
    #Etype = enemy type(based on True or False of this parameter, the enemy will be regular or will become a boss)
    def __init__(self, Ename, Etype, Ehealth, Especial_attack_points, Eattack_points, Edefense_points, Enormal_attack_vulnability, Erange_attack_vulnability, Emagic_attack_vulnability):
        self.name = Ename
        self.type = Etype
        self.health = Ehealth
        self.special_attack_points = Especial_attack_points
        self.attack_points = Eattack_points
        self.defense_points = Edefense_points
        self.normal_attack_vulnability = Enormal_attack_vulnability
        self.range_attack_vulnability = Erange_attack_vulnability
        self.magic_attack_vulnability = Emagic_attack_vulnability

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
    def magic_attack_vulnability(self, new_magic_attack_vulnability):
        self.range_attack_points =new_magic_attack_vulnability



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




