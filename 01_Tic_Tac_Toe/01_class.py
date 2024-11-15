import os


class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "] # 9 cells

    def display(self):  # Change for formatted print better
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("-----------")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("-----------")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")

    def update_cell(self, cell_number, player):
        # We substract 1 to get the actual cell the player is thinking of getting
        if self.cells[cell_number-1] != " ":
            return False
        else:
            self.cells[cell_number-1] = player
            return True


class Player():
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece


board = Board()  # Define this at tope and move classes to other files and import/use
player_1 = Player("Player 1", "X") # Change and define that data with players input
player_2 = Player("Player 2", "O")
players = [player_1, player_2]
game_over = False


def print_header():
    print("Welcome to Tic-Tac-Toe\n")


def refresh_screen():
    # Clear screen command depending on the OS
    os.system("cls" if os.name == "nt" else "clear")

    # Print header
    print_header()

    # Show the board
    board.display()

while not game_over:
    
    for player in players:

        refresh_screen()
        empty_cell = False

        while not empty_cell:
            # Get input:
            player_choice = int(input(f"\n{player.name}) Please choose 1 - 9. > "))
            # Update board
            empty_cell = board.update_cell(player_choice, player.piece)
            if not empty_cell:
                print("There's a piece in this position already")
