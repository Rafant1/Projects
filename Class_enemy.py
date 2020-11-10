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




