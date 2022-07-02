"""Function for validation."""

# Python
import re

# Local
from figures import possible_figures


def validate_position(position):
    """Validate position."""
    if (
        len(position) > 2
        or not re.match(r"[1-8]", position[1])
        or not re.match(r"[a-h]", position[0])
    ):
        return False
    return True


def validate_figure(figure):
    """Validate figure."""
    if figure not in possible_figures.keys():
        return False
    return True
