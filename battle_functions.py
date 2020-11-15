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