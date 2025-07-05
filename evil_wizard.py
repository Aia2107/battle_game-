import random
from character import Character

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen = random.randint(5, 15)
        self.health = min(self.health + regen, self.max_health)
        print(f"{self.name} regenerates {regen} health! Health is now {self.health}/{self.max_health}")
