from game_engine import create_character, battle
from evil_wizard import EvilWizard

def main():
    print("🧙 Welcome to the Battle Arena!")
    player = create_character()
    wizard = EvilWizard("Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
