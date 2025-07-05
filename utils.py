def get_user_choice(prompt, options):
    choice = input(prompt).strip()
    while choice not in options:
        print("Invalid option. Try again.")
        choice = input(prompt).strip()
    return choice
