class Player():
    def __init__(self, name: str, piece: str) -> None:
        """
        Initializes a new player.

        Attributes:
            name (str): player's name.
            piece (str): string used to display as the player's piece.
        """
        self.name = name
        self.piece = piece
