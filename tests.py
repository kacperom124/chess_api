"""Init tests."""

# Python
import pytest

# Flask
from flask import Flask

# Local
from board import BoardField
from figures import Bishop, King, Knight, Pawn, Rook
from routes import configure_routes
from validation import validate_figure, validate_position

all_fields = [f"{chr(96 + x)}{y}" for x in range(1, 9) for y in range(1, 9)]

possible_figures = [
    "king",
    "queen",
    "rook",
    "bishop",
    "knight",
    "pawn",
]


@pytest.mark.parametrize("test_input", all_fields)
def test_validate_position_true(test_input):  # noqa: D103
    assert validate_position(test_input)


@pytest.mark.parametrize("test_input", ["q1", "h9", "412"])
def test_validate_position_false(test_input):  # noqa: D103
    assert not validate_position(test_input)


@pytest.mark.parametrize("test_input", possible_figures)
def test_validate_figure_True(test_input):  # noqa: D103
    assert validate_figure(test_input)


possible_moves_data = [
    ("queen", "h1", 200),
    ("queen", "h9", 409),
    ("test", "h1", 404),
    ("queen", "q1", 409),
]


@pytest.mark.parametrize("figure, pos, res", possible_moves_data)
def test_possible_moves(figure, pos, res):
    """Test all figure and position for 200 response code."""
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    response = client.get(f"/api/v1/{figure}/{pos}")
    assert response.status_code == res


possibility_of_move_data = [
    ("queen", "h1", "h3", 200),
    ("queen", "h9", "q3", 409),
    ("queen", "h1", "t2", 409),
    ("test", "a2", "a1", 404),
]


@pytest.mark.parametrize("figure, pos, dest, res", possibility_of_move_data)
def test_possibility_of_move(figure, pos, dest, res):
    """Test all figure and position for 200 response code."""
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    response = client.get(f"/api/v1/{figure}/{pos}/{dest}")

    assert response.status_code == res


@pytest.mark.parametrize("x, y", [(1, 2)])
def test_boardfield_class_true(x, y):
    """Test magic methods for Boardfield. True ver."""
    field_1 = BoardField.create_valid_board(x, y)
    field_2 = BoardField.create_valid_board(x, y)
    assert field_1 == field_2
    assert str(field_1) == "a2"


@pytest.mark.parametrize("x, y", [(1, 2)])
def test_boardfield_class_false(x, y):
    """Test magic methods for Boardfield. False ver."""
    field_1 = BoardField.create_valid_board(x, y)
    field_2 = BoardField.create_valid_board(x + 1, y)
    assert field_1 != field_2
    assert str(field_1) != "h2"


@pytest.mark.parametrize("pos", ["a1"])
def test_king_class(pos):
    """Test available moves for King."""
    figure = King(pos)
    moves = [
        BoardField(1, 2),
        BoardField(2, 1),
        BoardField(2, 2),
    ]
    assert figure.position.x == 1 and figure.position.y == 1
    assert moves == figure.list_available_moves()


@pytest.mark.parametrize("pos", ["a1"])
def test_rook_class(pos):
    """Test available moves for Rook."""
    figure = Rook(pos)
    moves = [
        BoardField(2, 1),
        BoardField(3, 1),
        BoardField(4, 1),
        BoardField(5, 1),
        BoardField(6, 1),
        BoardField(7, 1),
        BoardField(8, 1),
        BoardField(1, 2),
        BoardField(1, 3),
        BoardField(1, 4),
        BoardField(1, 5),
        BoardField(1, 6),
        BoardField(1, 7),
        BoardField(1, 8),
    ]
    assert figure.position.x == 1 and figure.position.y == 1
    assert moves == figure.list_available_moves()


@pytest.mark.parametrize("pos", ["a1"])
def test_bishop_class(pos):
    """Test available moves for Bishop."""
    figure = Bishop(pos)
    moves = [
        BoardField(2, 2),
        BoardField(3, 3),
        BoardField(4, 4),
        BoardField(5, 5),
        BoardField(6, 6),
        BoardField(7, 7),
        BoardField(8, 8),
    ]
    assert figure.position.x == 1 and figure.position.y == 1
    assert moves == figure.list_available_moves()


@pytest.mark.parametrize("pos", ["a1"])
def test_knight_class(pos):
    """Test available moves for Knight."""
    figure = Knight(pos)
    moves = [
        BoardField(2, 3),
        BoardField(3, 2),
    ]
    assert figure.position.x == 1 and figure.position.y == 1
    assert moves == figure.list_available_moves()


@pytest.mark.parametrize("pos", ["a1"])
def test_pawn_class(pos):
    """Test available moves for Pawn."""
    figure = Pawn(pos)
    moves = [
        BoardField(1, 2),
    ]
    assert figure.position.x == 1 and figure.position.y == 1
    assert moves == figure.list_available_moves()
