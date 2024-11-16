def main():
    pass

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



# garantiza que el flujo principal solo se ejecute si el archivo se ejecuta directamente y no cuando es importado.
if __name__ == "__main__": # When the if statement evaluates to True, the Python interpreter executes main().
    main()

# __name__ special variable,

# repr() displays representation of an object
#repr(__name__)




board = Board()  # Define this at tope and move classes to other files and import/use
# Change and define that data with players input
player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")
players = [player_1, player_2]
game_over = False