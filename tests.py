"""Init tests."""

# Python
import pytest

# Local
from validation import validate_figure, validate_position

all_fields = [f'{chr(96 + x)}{y}' for x in range(1, 9) for y in range(1, 9)]


@pytest.mark.parametrize('test_input',
                         all_fields)
def test_validate_position_true(test_input):
    assert validate_position(test_input)


@pytest.mark.parametrize('test_input',
                         ['q1', 'h9', '412'])
def test_validate_position_false(test_input):
    assert not validate_position(test_input)


possible_figures = [
    'king',
    'queen',
    'rook',
    'bishop',
    'knight',
    'pawn',
]


@pytest.mark.parametrize('test_input',
                         possible_figures)
def test_validate_figure_True(test_input):
    assert validate_figure(test_input)
