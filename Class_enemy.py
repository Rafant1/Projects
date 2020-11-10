import random




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


