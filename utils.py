"""Utils functions."""

# Python
from json import dumps

# Flask
from flask import Response


def response(data: dict, code: int) -> Response:  # noqa

    return Response(
        response=dumps(data),
        mimetype='application/json',
        status=code,
    )
