import os

def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def refresh_screen():
    # Clear screen command depending on the OS
    os.system("cls" if os.name == "nt" else "clear")

    # Print header
    print_header()

    # Show the board
    board.display()
