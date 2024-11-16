import os


class Player():
    def __init__(self, name, piece):
        self.name = name
        self.piece = piece


class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # 9 cells
        self.winner = None
        self.is_full = False

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
    
    def update_full(self):
        filtrado = filter(lambda cell: cell is " ", self.cells)
        if (len(filtrado) == 0):
            self.is_full = True

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def is_winner(self, player: Player):
        if self.cells[0] == player.piece and self.cells[1] == player.piece and self.cells[2] == player.piece:
            self.winner= player.name
            return True
"""         elif self.cells[0] == player.piece and self.cells[1] == player.piece and self.cells[2] == player.piece:
            self.winner= player.name
            return True
        elif self.cells[0] == player.piece and self.cells[1] == player.piece and self.cells[2] == player.piece:
            self.winner= player.name
            return True """





board = Board()  # Define this at tope and move classes to other files and import/use
# Change and define that data with players input
player_1 = Player("Player 1", "X")
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

        # Check if is a winner
        game_over = board.is_winner(player)
        board.update_full()
        game_over = board.is_full

# Comprobar por aquí que no es tie tampoco
        empty_cell = False
        if not game_over:
            while not empty_cell:
                # Get input:
                player_choice = int(
                    input(f"\n{player.name}) Please choose 1 - 9. > "))
                # Update board
                empty_cell = board.update_cell(player_choice, player.piece)
                if not empty_cell:
                    print("There's a piece in this position already")


# Modificar, jutno con is full, update full, is_full etc
print(f"The winner is: {board.winner}")
play_again = raw_input("Would you like to play again [Y] Yes [N] No) > ")
if play_again == "Y":
    continue
else:
    break

# lesson 4

# Board method
# Checks for a tie
def is_tie(self):
    used_cells = 0
    for cell in self.cells:
        if cell != " ":
            used_cells +=1
    if used_cells == 9:
        return True
    else:
        return False
    
# lesson 5: AI moves

# Board method, introducir no fluxo do xogo
def ai_move(self, player):

    if player == "X":
        enemy = "O"
    if player == "O":
        enemy = "X"

    # If the center is open, choose that
    if self.cells[4] == " ":
        self.update_cell(4, player)
    elif
    # AI blocks

    # AI can win

    # Choose random, import random better
    for i in range(9):
        if self.cells[i] == " ":
            self.update_cell(i, player)
            breack

# last lesson: https://www.youtube.com/watch?v=8t9ou2I0IOE&list=PLlEgNdBJEO-m6o4INllCF1FRMS262A5C_&index=6&ab_channel=TokyoEdtech