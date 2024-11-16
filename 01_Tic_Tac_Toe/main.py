import utils
from board import Board
from player import Player

utils.print_header()


board = Board()

# Change and define this data with players input
player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")
players = [player_1, player_2]
game_over = False


def main():
    pass


while not game_over:

    for player in players:

        utils.refresh_screen()

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


print(f"The winner is: {board.winner}")
play_again = raw_input("Would you like to play again [Y] Yes [N] No) > ")
if play_again == "Y":
    pass
    # continue
else:
    pass
    # break


# garantiza que el flujo principal solo se ejecute si el archivo se ejecuta directamente y no cuando es importado.
# When the if statement evaluates to True, the Python interpreter executes main().
if __name__ == "__main__":
    main()

# __name__ special variable,

# repr() displays representation of an object
# repr(__name__)
