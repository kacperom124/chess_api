"""Classes for board."""


class BoardField:
    """Board field class."""

    def __init__(self, x: int, y: int):  # noqa: D107
        self.x = x
        self.y = y

    @classmethod
    def create_valid_board(cls, x: int, y: int):
        """Check if x and y can be on board."""
        if (0 < x < 9) and (0 < y < 9):
            return cls(x, y)

    def __eq__(self, other_board):
        """Comparison two boards."""
        return (self.x == other_board.x) and (self.y == other_board.y)

    def __str__(self):
        """Return string in format: a1, b2."""
        return f'{chr(96 + self.x)}{self.y}'
