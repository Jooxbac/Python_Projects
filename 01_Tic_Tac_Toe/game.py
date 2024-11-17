from board import Board
from player import Player
import os


class Game():
    def __init__(self) -> None:
        """
        Initializes a new game.

        Attributes:
            name (str): player's name.
            piece (str): string used to display as the player's piece.
        """
        self.board = Board()
        self.player_1 = Player("Player 1", "X")
        self.player_2 = Player("Player 2", "O")
        self.players = [self.player_1, self.player_2]
        self.is_game_over = False
        self.turn = 0

    def print_header(self):
        print("Welcome to Tic-Tac-Toe\n")

    def refresh_screen(self):
        # Clear screen command depending on the OS
        os.system("cls" if os.name == "nt" else "clear")

        # Print header
        self.print_header()

        # Show the board
        self.board.display()

        print(f"Turn {self.turn} ended.")

        if self.turn == 9 and not self.is_game_over:
            print("It's a tie")

    def start_new_game(self):
        # Esto debería crear una nueva instancia de juego y destruir la anterior, si la hay, no ser un método de Game como tal.
        while not self.is_game_over:
            for player in self.players:
                self.refresh_screen()
                # board.update_full()
                # is_game_over = board.is_full
                empty_cell = False

                print(f"{self.is_game_over}")
                if not self.is_game_over:

                    while not empty_cell:
                        # Get input:
                        player_choice = int(
                            input(f"\n{player.name}) Please choose 1 - 9. > "))
                        # Update board
                        empty_cell = self.board.update_cell(
                            player_choice, player.piece)

                    self.turn += 1
                    self.is_game_over = self.board.check_for_winner(player)

                else:
                    play_again = input(
                        "Would you like to play again [Y] Yes [N] No) > ")
                    if play_again == "Y":
                        print("Comenzar nueva partida")
                        # self.start_new_game()
                    else:
                        exit()

        print(f"There is a winner: {self.board.winner}")
