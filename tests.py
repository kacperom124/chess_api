"""Init tests."""

# Python
import pytest

# Flask
from flask import Flask

# Local
from routes import configure_routes
from validation import validate_position, validate_figure

all_fields = [f'{chr(96 + x)}{y}' for x in range(1, 9) for y in range(1, 9)]

possible_figures = [
    'king',
    'queen',
    'rook',
    'bishop',
    'knight',
    'pawn',
]


@pytest.mark.parametrize('test_input', all_fields)
def test_validate_position_true(test_input):
    assert validate_position(test_input)


@pytest.mark.parametrize('test_input', ['q1', 'h9', '412'])
def test_validate_position_false(test_input):
    assert not validate_position(test_input)


@pytest.mark.parametrize('test_input', possible_figures)
def test_validate_figure_True(test_input):
    assert validate_figure(test_input)

possible_moves_data = [
    ('queen', 'h1', 200),
    ('queen', 'h9', 409),
    ('test', 'h1', 404),
    ('queen', 'q1', 409),
]


@pytest.mark.parametrize('figure, pos, res', possible_moves_data)
def test_possible_moves(figure, pos, res):
    """Test all figure and position for 200 response code."""
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    response = client.get(f'/api/v1/{figure}/{pos}')
    assert response.status_code == res


possibility_of_move_data = [
    ('queen', 'h1', 'h3', 200),
    ('queen', 'h9', 'q3', 409),
    ('queen', 'h1', 't2', 409),
    ('test', 'a2', 'a1', 404),
]


@pytest.mark.parametrize('figure, pos, dest, res', possibility_of_move_data)
def test_possibility_of_move(figure, pos, dest, res):
    """Test all figure and position for 200 response code."""
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    response = client.get(f'/api/v1/{figure}/{pos}/{dest}')

    assert response.status_code == res
