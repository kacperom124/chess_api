"""Function for validation."""

# Python
import re


def validate_position(position):
    if len(position) > 2 or not re.match(r'[1-8]', position[1]) or not re.match(r'[a-h]', position[0]):
        return False
    return True


def validate_figure(figure):
    if figure not in [chr(i) for i in range(97, 105)]:
        return False
    return True
