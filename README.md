==============================
🧙‍♂️ TURN-BASED BATTLE GAME
==============================

Welcome to the Turn-Based Battle Game!
You play as a hero of your choice and face off against the evil Dark Wizard in a strategic, turn-based combat.

-------------------------
🎮 HOW TO PLAY
-------------------------

1. Run the main script:
   > python main.py

2. Choose your character class:
   - Warrior: Strong and defensive fighter
   - Mage: Powerful magic user with fireballs
   - Archer: Fast and nimble with double-shot skills
   - Paladin: Balanced class with healing and shields

3. In each turn, choose one of the following actions:
   - Attack
   - Use Special Ability 1
   - Use Special Ability 2
   - Heal
   - View Stats

4. The Evil Wizard will regenerate and counterattack each round.

5. Battle continues until either you or the wizard is defeated.

-------------------------
🧱 PROJECT STRUCTURE
-------------------------

battle_game/
├── main.py               # Entry point to start the game
├── character.py          # Contains base Character class
├── abilities.py          # Contains special abilities for each class
├── evil_wizard.py        # EvilWizard enemy class with health regen
├── game_engine.py        # Handles gameplay flow and battle logic
├── utils.py              # Small helper functions like input validation
└── README.txt            # This file

-------------------------
💡 FEATURES
-------------------------

✔️ 4 Playable classes with unique abilities  
✔️ Randomized attack and heal values  
✔️ Healing and shielding mechanics  
✔️ Turn-based combat logic  
✔️ Victory and defeat messages  
✔️ Modular, readable file structure

-------------------------
🚀 BONUS IDEAS TO TRY
-------------------------

- Add leveling system and experience points
- Create multiple enemy waves or mini-bosses
- Add inventory system (potions, weapons)
- Build a GUI using `tkinter` or `pygame`

-------------------------
📌 REQUIREMENTS
-------------------------

- Python 3.x
- No third-party packages needed

-------------------------
🔗 AUTHOR & LICENSE
-------------------------

Created as part of a programming project.
Feel free to modify and extend it!

