"""Main app."""

# Flask
import json

from flask import Flask

# Local
from board import BoardField
from figures import possible_figures
from validation import validate_figure, validate_position

app = Flask(__name__)


def response(data, code):
    temp_response = app.response_class(
        response=json.dumps(data),
        mimetype='application/json',
        status=code
    )
    return temp_response


@app.route('/api/v1/<figure>/<position>')
def possible_moves(figure, position):
    """Possible moves api."""
    response_data = {
        'availableMoves': [],
        'error': None,
        'figure': figure,
        'currentField': position,
    }
    # Validation
    if not validate_position(position):
        response_data['error'] = 'Field does not exist'
        return response(response_data, 409)
    if not validate_figure(figure):
        response_data['error'] = 'Figure does not exist'
        return response(response_data, 404)
    actual_figure = possible_figures[figure](position)
    response_data['availableMoves'] = [
        str(move) for move in actual_figure.list_available_moves()
    ]

    return response(response_data, 200)


@app.route('/api/v1/<figure>/<current_position>/<destination_position>')
def check_possibility_of_move(figure, current_position, destination_position):
    """Check possibility of moves."""
    response_data = {
        'move': None,
        'error': None,
        'figure': figure,
        'currentField': current_position,
        'destField': destination_position,
    }
    # Validation
    if not validate_position(current_position):
        response_data['error'] = 'Current field does not exist'
        return response(response_data, 409)
    if not validate_position(destination_position):
        response_data['error'] = 'Destination field does not exist'
        return response(response_data, 409)
    if not validate_figure(figure):
        response_data['error'] = 'Figure does not exist'
        return response(response_data, 404)

    actual_figure = possible_figures[figure](current_position)
    destination_position = possible_figures[figure]\
        (destination_position).position
    if actual_figure.validate_move(destination_position):
        response_data['move'] = 'valid'
    else:
        response_data['move'] = 'invalid'
    return response(response_data, 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
