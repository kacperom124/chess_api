"""Main app."""

# Flask
from flask import Flask

# Local
from board import BoardField
from figures import possible_figures
from validation import validate_position
from validation import validate_figure

app = Flask(__name__)


@app.route('/api/v1/<figure>/<position>')
def possible_moves(figure, position):
    response_data = {
        'availableMoves': [],
        'error': None,
        'figure': figure,
        'currentField': position
    }
    # Validation
    if not validate_position(position):
        response_data['error'] = 'Field does not exist'
        return response_data
    if not validate_figure(figure):
        response_data['error'] = 'Figure does not exist'
        return response_data

    actual_figure = possible_figures[figure](position)

    response_data['availableMoves'] = [str(move) for move in actual_figure.list_available_moves()]

    return response_data


@app.route('/api/v1/<figure>/<current_position>/<destination_position>')
def check_possibility_of_move(figure, current_position, destination_position):
    response_data = {
        'move': None,  # to zapytania czy to powinno zostać
        'error': destination_position,
        'figure': figure,
        'currentField': current_position,
        'destField': destination_position
    }
    # Validation
    if not validate_position(current_position):
        response_data['error'] = 'Current field does not exist'
        return response_data
    if not validate_position(destination_position):
        response_data['error'] = 'Destination field does not exist'
        return response_data
    if not validate_figure(figure):
        response_data['error'] = 'Figure does not exist'
        return response_data

    actual_figure = possible_figures[figure](current_position)
    destination_position = BoardField.create_valid_board(destination_position)
    if actual_figure.validate_move(destination_position):
        response_data['move'] = 'valid'
    else:
        response_data['move'] = 'invalid'
    return response_data


if __name__ == '__main__':
    app.run(debug=True)
