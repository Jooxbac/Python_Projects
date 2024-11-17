from board import Board
from player import Player


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
        self.players = [player_1, player_2]
        self.is_game_over = False

    def start_new_game():
        while not is_game_over:
            for player in players:
                refresh_screen(board)
                # board.update_full()
                # is_game_over = board.is_full
                empty_cell = False

                if not is_game_over:

                    while not empty_cell:
                        # Get input:
                        player_choice = int(
                            input(f"\n{player.name}) Please choose 1 - 9. > "))
                        # Update board
                        empty_cell = board.update_cell(
                            player_choice, player.piece)

                    is_game_over = board.check_for_winner(player)

        print(f"There is a winner: {board.winner}")
