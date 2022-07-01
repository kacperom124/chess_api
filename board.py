"""Classes for board."""

board_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')  # sprawa board_letters


class Board:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def create_valid_board(cls, x: int, y: int):
        if (x > 0 and x < 9) and (y > 0 and y < 9):
            return cls(x, y)

    def __eq__(self, other_board):
        return (self.x == other_board.x) and (self.y == other_board.y)

    def __str__(self):
        return f'{board_letters[self.x - 1]}{self.y}'

    def toJSON(self):  # wtf
        return str(self)
