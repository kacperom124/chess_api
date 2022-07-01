"""Classes for all chess piece"""

# Local
from board import BoardField


class SuperFigure:

    def __init__(self, position: str):
        self.position = BoardField(ord(position[0]) - 96, int(position[1]))

    def list_available_moves(self) -> list:
        pass

    def validate_move(self, move: BoardField) -> bool:
        if move in self.list_available_moves():
            return True
        return False

    def in_bound(self):
        pass


class King(SuperFigure):

    def list_available_moves(self) -> list:
        available_moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                new_move = BoardField.create_valid_board(self.position.x + x, self.position.y + y)
                if new_move:
                    if new_move != self.position:
                        available_moves.append(new_move)
        return available_moves


class Rook(SuperFigure):

    def list_available_moves(self) -> list:
        moves = []
        i = 1

        while True:  # left
            next_pos = BoardField.create_valid_board(self.position.x - i, self.position.y)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # right
            next_pos = BoardField.create_valid_board(self.position.x + i, self.position.y)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # up
            next_pos = BoardField.create_valid_board(self.position.x, self.position.y + i)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # down
            next_pos = BoardField.create_valid_board(self.position.x, self.position.y - i)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        return moves


class Bishop(SuperFigure):

    def list_available_moves(self) -> list:
        moves = []
        i = 1
        while True:  # left up
            next_pos = BoardField.create_valid_board(self.position.x - i, self.position.y - i)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # left down
            next_pos = BoardField.create_valid_board(self.position.x - i, self.position.y + i)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # right up
            next_pos = BoardField.create_valid_board(self.position.x + i, self.position.y - i)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # right down
            next_pos = BoardField.create_valid_board(self.position.x + i, self.position.y + i)
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        return moves


class Knight(SuperFigure):
    move_options = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

    def list_available_moves(self) -> list:
        moves = []
        for move_option in self.move_options:  # can be done on list comprehension but is very ugly.
            new_pos = BoardField.create_valid_board(self.position.x + move_option[0], self.position.y + move_option[1])
            if new_pos:
                moves.append(new_pos)
        return moves


class Pawn(SuperFigure):

    def list_available_moves(self) -> list:
        moves = []
        if self.position.y == 2:
            moves.append(BoardField.create_valid_board(self.position.x, self.position.y + 2))
        next_pos = BoardField.create_valid_board(self.position.x, self.position.y + 1)
        if next_pos:
            moves.append(next_pos)
        return moves


class Queen(SuperFigure):

    def list_available_moves(self) -> list:
        """Take moves from rook and bishop."""
        return Rook(str(self.position)).list_available_moves() + Bishop(str(self.position)).list_available_moves()


possible_figures = {
    'king': King,
    'queen': Queen,
    'rook': Rook,
    'bishop': Bishop,
    'knight': Knight,
    'pawn': Pawn,
}
