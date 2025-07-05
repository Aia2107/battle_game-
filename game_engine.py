from evil_wizard import EvilWizard
from utils import get_user_choice
from character import Character
from abilities import WarriorAbilities, MageAbilities, ArcherAbilities, PaladinAbilities

class Warrior(Character, WarriorAbilities):
    def __init__(self, name):
        super().__init__(name, 140, 25)

class Mage(Character, MageAbilities):
    def __init__(self, name):
        super().__init__(name, 100, 35)

class Archer(Character, ArcherAbilities):
    def __init__(self, name):
        super().__init__(name, 110, 20)

class Paladin(Character, PaladinAbilities):
    def __init__(self, name):
        super().__init__(name, 130, 20)

def create_character():
    print("Choose your character class:")
    print("1. Warrior\n2. Mage\n3. Archer\n4. Paladin")
    choice = input("Enter class number: ")
    name = input("Enter your character's name: ")

    if choice == '1': return Warrior(name)
    elif choice == '2': return Mage(name)
    elif choice == '3': return Archer(name)
    elif choice == '4': return Paladin(name)
    else:
        print("Invalid input. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack\n2. Special Ability 1\n3. Special Ability 2\n4. Heal\n5. View Stats")
        choice = input("Your action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_1(wizard)
        elif choice == '3':
            player.special_2()
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice.")

        if wizard.health > 0:
            print("\n--- Wizard's Turn ---")
            wizard.regenerate()
            wizard.attack(player)

    if player.health <= 0:
        print(f"\n💀 {player.name} was defeated by {wizard.name}. Evil wins.")
    else:
        print(f"\n🎉 {player.name} has defeated the dark wizard {wizard.name}!")

