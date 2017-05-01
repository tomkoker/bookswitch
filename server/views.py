import sqlite3
import bcrypt

from flask import request, jsonify, session, abort

from server import app
from db import query_db

from models.user import User
from models.book import Book
from models.listing import Listing



@app.route('/api/all')
def all_listings():
    return jsonify([listing.serialized() for listing in Listing.all()])


@app.route('/api/users')
def all_users():
    return jsonify(User.all())


@app.route('/api/signup', methods=['POST'])
def signup():
    if (not request.json or 'email' not in request.json or
            'password' not in request.json or
            'username' not in request.json):
        abort(400)

    if User.with_email(request.json['email']) is not None:
        # report user with email already exists
        return jsonify({'status': 'failed'})

    if User.with_username(request.json['username'] is not None):
        # report user with username already exists
        return jsonify({'status': 'failed'})

    # save user to database
    User.add(request.json['username'], request.json['email'],
             User.hash_password(request.json['password']))

    # registration was successful
    return jsonify({'status': 'success'})


@app.route('/api/login', methods=['POST'])
def login():
    if (not request.json or 'username' not in request.json or
            'password' not in request.json):
        abort(400)

    user = User.with_username(request.json['username'])

    if user is None:
        # report wrong username
        return jsonify({'status': 'failed'})

    if user.check_password(request.json['password']):
        # login successful
        session["user_id"] = user.id
        return jsonify({'status': 'success'})

    # report wrong password
    return jsonify({'status': 'failed'})


@app.route('/api/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'status': 'success'})


@app.route('/api/new-listing', methods=['POST'])
def new_listing():

    book = Book.with_isbn(request.json['listing']['book']['isbn'])
    if book is None:
        Book.add(request.json['listing']['book']['isbn'],
                    request.json['listing']['book']['title'])
        book = Book.with_isbn(request.json['listing']['book']['isbn'])

    Listing.add(book, request.json['listing']['price'])

    return jsonify({'status': 'success'})


def me():
    if 'user_id' in session:
        return jsonify({'status': 'success'},
                       {'data': {'authenticated': True}})
    return jsonify({'status': 'success'},
                   {'data': {'authenticated': False}})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    Catch all that redirects to index.html for the single page application
    """
    return app.send_static_file('index.html')
