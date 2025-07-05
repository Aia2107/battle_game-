import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack_power = attack_power
        self.block_next_attack = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if opponent.block_next_attack:
            print(f"{opponent.name} blocked the attack!")
            opponent.block_next_attack = False
        else:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = random.randint(10, 20)
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} heals for {heal_amount}. Health is now {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name} - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

