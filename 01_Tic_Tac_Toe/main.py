from game import Game

game = Game()
game.start_new_game()

# Aplicar patrón singleton, para que sólamente exista una instancia de juego.


def main():
    pass


if False:
    # garantiza que el flujo principal solo se ejecute si el archivo se ejecuta directamente y no cuando es importado.
    # When the if statement evaluates to True, the Python interpreter executes main().
    if __name__ == "__main__":
        main()

    # __name__ special variable,

    # repr() displays representation of an object
    # repr(__name__)
