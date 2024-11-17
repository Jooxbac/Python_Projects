from utils import start_game
from board import Board
from player import Player
from game import Game

game = Game()
game.start_new_game()

def main():
    pass


if False:

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
