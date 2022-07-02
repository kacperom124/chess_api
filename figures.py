"""Classes for all chess piece."""

# Python
from typing import List

# Local
from board import BoardField


class SuperFigure:
    """Parent class for all figures."""

    def __init__(self, position: str):  # noqa: D107
        self.position = BoardField(ord(position[0]) - 96, int(position[1]))

    def list_available_moves(self) -> List[BoardField]:
        """Must be implemented in children class."""
        pass

    def validate_move(self, move: BoardField) -> bool:
        """Check if move is possible."""
        if move in self.list_available_moves():
            return True
        return False


class King(SuperFigure):
    """Class for king figure."""

    def list_available_moves(self) -> List[BoardField]:
        """Return surrounding fields."""
        available_moves = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                new_move = BoardField.create_valid_board(
                    self.position.x + x,
                    self.position.y + y,
                )
                if new_move:
                    if new_move != self.position:
                        available_moves.append(new_move)
        return available_moves


class Rook(SuperFigure):
    """Class for rook figure."""

    def list_available_moves(self) -> List[BoardField]:
        """Return cross of fields."""
        moves = []
        i = 1

        while True:  # left
            next_pos = BoardField.create_valid_board(
                self.position.x - i,
                self.position.y,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # right
            next_pos = BoardField.create_valid_board(
                self.position.x + i,
                self.position.y,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # up
            next_pos = BoardField.create_valid_board(
                self.position.x,
                self.position.y + i,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # down
            next_pos = BoardField.create_valid_board(
                self.position.x,
                self.position.y - i,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        return moves


class Bishop(SuperFigure):
    """Class for bishop figure."""

    def list_available_moves(self) -> List[BoardField]:
        """Return fields in shape of X."""
        moves = []
        i = 1
        while True:  # left up
            next_pos = BoardField.create_valid_board(
                self.position.x - i,
                self.position.y - i,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # left down
            next_pos = BoardField.create_valid_board(
                self.position.x - i,
                self.position.y + i,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # right up
            next_pos = BoardField.create_valid_board(
                self.position.x + i,
                self.position.y - i,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        while True:  # right down
            next_pos = BoardField.create_valid_board(
                self.position.x + i,
                self.position.y + i,
            )
            if next_pos:
                moves.append(next_pos)
                i += 1
            else:
                i = 1
                break

        return moves


class Knight(SuperFigure):
    """Class for knight figure."""

    move_options = (
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
    )

    def list_available_moves(self) -> List[BoardField]:
        """Return fields in range of L(2.1)."""
        moves = []  # can be done on list comprehension but is very ugly.
        for move_option in self.move_options:
            new_pos = BoardField.create_valid_board(
                self.position.x + move_option[0],
                self.position.y + move_option[1],
            )
            if new_pos:
                moves.append(new_pos)
        return moves


class Pawn(SuperFigure):
    """Class for pawn figure."""

    def list_available_moves(self) -> List[BoardField]:
        """Pawn can go 1 forward or 2 forward(only on start)."""
        moves = []
        if self.position.y == 2:  # first move
            moves.append(
                BoardField.create_valid_board(
                    self.position.x,
                    self.position.y + 2,
                ),
            )

        next_pos = BoardField.create_valid_board(
            self.position.x,
            self.position.y + 1,
        )
        if next_pos:
            moves.append(next_pos)
        return moves


class Queen(SuperFigure):
    """Class for queen figure."""

    def list_available_moves(self) -> List[BoardField]:
        """Take moves from rook and bishop."""
        return (
            Rook(str(self.position)).list_available_moves()
            + Bishop(str(self.position)).list_available_moves()
        )


possible_figures = {
    'king': King,
    'queen': Queen,
    'rook': Rook,
    'bishop': Bishop,
    'knight': Knight,
    'pawn': Pawn,
}
