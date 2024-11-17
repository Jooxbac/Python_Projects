from player import Player


class Board():
    def __init__(self) -> None:
        """
        Initializes a new game board.

        Attributes:
            cells (list[str]): list of 9 strings representing the cells of the board.
            is_full (bool): indicates whether the board is full.
            is_tie (bool): indicates whether the game ended in a tie.
            winner (str | None): the winner of the game, or None if there is no winner yet.
            win_combinations (list[list[str]]): possible combinations that win the game.
        """
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  # 9 cells
        self.is_full = False
        self.is_tie = False
        self.winner = None
        self.win_combinations = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9],
            [1, 2, 3],
            [1, 5, 9],
            [3, 5, 7],
        ]

    def ai_move(self, player) -> None:
        """
        TODO
        Movements done by the computer when playing against it.

        Attributes:
            player (str): lis

        Returns:
            None: does not return a value.
        """
        if player == "X":
            enemy = "O"
        if player == "O":
            enemy = "X"

        # If the center is open, choose that
        if self.cells[4] == " ":
            self.update_cell(4, player)
        elif True:
            pass

        # AI blocks

        # AI can win

        # Choose random, import random better
        for i in range(9):
            if self.cells[i] == " ":
                self.update_cell(i, player)
                break

    def display(self) -> None:
        """
        Displays the board.

        Returns:
            None: does not return a value.
        """
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("-----------")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("-----------")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")

        # Checks for a tie
    def is_tie(self) -> bool:
        """
        TODO
        Checks if the game ended with a tie.

        Returns:
            None: does not return a value.
        """
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def check_for_winner(self, player: Player) -> bool:
        """
        Checks if a player has won the game.

        Args:
            player (Player): player we check if has won.

        Returns:
            bool: True if the player has won, False if not.
        """
        is_win_combination = False

        for combination in self.win_combinations:

            if not is_win_combination:
                pieces_counter = 0

                for cell_number in combination:

                    if self.cells[cell_number-1] == player.piece:
                        pieces_counter += 1

                    if pieces_counter == 3:
                        is_win_combination = True
                        self.winner = player.name

        return is_win_combination

    def reset(self) -> None:
        """
        Resets the board, emptying all of the board's cells.

        Returns:
            None: does not return a value.
        """
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def update_cell(self, cell_number: int, player_piece: str) -> bool:
        """
        Updates a cell if it's possible

        Args:
            cell_number (int): cell to be updated.
            player_piece (str): piece to be set into the cell.

        Returns:
            bool: True if cell is updatable, False if not.

        Raises:
            IndexError: when passed a number that is not between 1 and 9.
        """
        try:
            # We substract 1 to get the actual cell the player is thinking of getting
            if self.cells[cell_number-1] != " ":
                print("There's a piece in this position already")
                return False
            else:
                self.cells[cell_number-1] = player_piece
                return True
        except IndexError:
            print("Given value must be between 1 and 9")
            return False

    def update_full(self) -> None:
        """
        Updates the is_full attribute of the instance, by checking if there are not empty cells.

        Returns:
            None: does not return a value.
        """
        empty_cells = filter(lambda cell: cell is " ", self.cells)
        if (len(empty_cells) == 0):
            self.is_full = True
