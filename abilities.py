class WarriorAbilities:
    def special_1(self, opponent):
        print(f"{self.name} uses 'Berserker Rage'!")
        self.attack_power += 10
        self.attack(opponent)
        self.attack_power -= 10

    def special_2(self):
        print(f"{self.name} uses 'War Cry' to block the next attack!")
        self.block_next_attack = True


class MageAbilities:
    def special_1(self, opponent):
        print(f"{self.name} casts 'Fireball'!")
        damage = 30
        opponent.health -= damage
        print(f"Fireball hits {opponent.name} for {damage} damage!")

    def special_2(self):
        print(f"{self.name} casts 'Magic Barrier' to block the next attack!")
        self.block_next_attack = True


class ArcherAbilities:
    def special_1(self, opponent):
        print(f"{self.name} uses 'Quick Shot'!")
        for _ in range(2):
            self.attack(opponent)

    def special_2(self):
        print(f"{self.name} uses 'Evade' to dodge the next attack!")
        self.block_next_attack = True


class PaladinAbilities:
    def special_1(self, opponent):
        print(f"{self.name} uses 'Holy Strike'!")
        damage = self.attack_power + 15
        opponent.health -= damage
        print(f"Holy Strike deals {damage} damage to {opponent.name}!")

    def special_2(self):
        print(f"{self.name} uses 'Divine Shield' to block the next attack!")
        self.block_next_attack = True
