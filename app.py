"""Main app."""

# Python
import re

# Flask
from flask import Flask

# Local
from board import Board
from figures import possible_figures

app = Flask(__name__)

board_letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def validate_position(position):
    if len(position) > 2 or not re.match(r'[1-8]', position[1]) or not re.match(r'[a-h]', position[0]):
        return False
    return True


def validate_figure(figure):
    if figure not in possible_figures.keys():
        return False
    return True


@app.route('/api/v1/<figure>/<position>')
def possible_moves(figure, position):
    response_data = {
        'availableMoves': [],
        'error': None,
        'figure': figure,
        'currentField': position
    }
    if not validate_position(position):
        response_data['error'] = 'Field does not exist'
        return response_data
    if not validate_figure(figure):
        response_data['error'] = 'Figure does not exist'
        return response_data

    actual_figure = possible_figures[figure](
        board_letters.index(position[0]) + 1,
        int(position[1])
    )

    move_list = [] # Nie chce się serialzować to jsona
    for move in actual_figure.list_available_moves():
        move_list.append(str(move))
    response_data['availableMoves'] = move_list
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
    if not validate_position(current_position):
        response_data['error'] = 'Current field does not exist'
        return response_data
    if not validate_position(destination_position):
        response_data['error'] = 'Destination field does not exist'
        return response_data
    if not validate_figure(figure):
        response_data['error'] = 'Figure does not exist'
        return response_data
    actual_figure = possible_figures[figure](
        board_letters.index(current_position[0]) + 1,
        int(current_position[1])
    )
    destination_position = Board.create_valid_board(
        board_letters.index(destination_position[0]) + 1,
        int(destination_position[1])
    )
    possibility = actual_figure.validate_move(destination_position)
    if possibility:
        response_data['move'] = 'valid'
    else:
        response_data['move'] = 'invalid'
    return response_data


if __name__ == '__main__':
    app.run(debug=True)
