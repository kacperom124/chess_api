"""Classes for board."""


class BoardField:
    """Board field class."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def create_valid_board(cls, x: int, y: int):
        """Check if x and y can be on board."""
        if (0 < x < 9) and (0 < y < 9):
            return cls(x, y)

    def __eq__(self, other_board):
        return (self.x == other_board.x) and (self.y == other_board.y)

    def __str__(self):
        return f'{chr(96 + self.x)}{self.y}'

    def toJSON(self):  # wtf
        return str(self)
