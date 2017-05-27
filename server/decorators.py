import functools
from flask import jsonify, session, abort


def jsonapi(f):
    """This decorator generates an API response from a dictionary or
    model, and a status string."""

    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        status, data = f(*args, **kwargs)

        return jsonify({
            'status': status,
            'data': data
        })

    return wrapped


def auth(f):
    """This decorator implements authentication for views"""

    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        if not session.get('user_id'):
            abort(401)

        return f(*args, **kwargs)
    return wrapped
