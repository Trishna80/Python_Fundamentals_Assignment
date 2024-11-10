import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_input(prompt):
    """Gets input from the user with a prompt."""
    return input(prompt)
