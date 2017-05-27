import bcrypt

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(13), unique=True)
    title = db.Column(db.String(128))
    listings = db.relationship("Listing", back_populates="book")

    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title

    def __repr__(self):
        return '<Book %r>' % (self.title)

    def serialized(self):
        return {'title': self.title, 'isbn': self.isbn}


class Listing(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    book = db.relationship("Book")

    def __init__(self, price):
        self.price = price

    def __repr__(self):
        return '<Listing>'

    def serialized(self):
        return {'book': self.book.serialized(), 'price': self.price}


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.Text)
    active = db.Column(db.Boolean)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'),
                                      bcrypt.gensalt())
        self.active = False

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),
                              self.password.encode('utf-8'))

    def __repr__(self):
        return '<User %r>' % (self.username)

    def activate(self):
        self.active = True
        db.session.commit()

    @staticmethod
    def username_taken(username):
        return db.session.query(
            db.exists().where(User.username == username)).scalar()

    @staticmethod
    def email_taken(email):
        return db.session.query(
            db.exists().where(User.email == email)).scalar()
