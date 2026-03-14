import os

def clear_screen():
    # Clear the console screen based on the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:
        os.system('clear')

def pause():
    input("Press Enter to continue...")