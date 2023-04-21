class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)

class Enemy(Character):
    pass

player = Character("Player", 100, 10)
enemy = Enemy("Enemy", 50, 5)

while player.health > 0 and enemy.health > 0:
    player.attack_enemy(enemy)
    print(f"{player.name} attacked {enemy.name} for {player.attack} damage.")
    if enemy.health <= 0:
        print(f"{enemy.name} has been defeated!")
        break
    enemy.attack_enemy(player)
    print(f"{enemy.name} attacked {player.name} for {enemy.attack} damage.")
    if player.health <= 0:
        print(f"{player.name} has been defeated!")
        break

