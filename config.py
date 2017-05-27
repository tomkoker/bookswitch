import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, "database.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "secret"

# Mail settings

MAIL_SENDER = 'do-not-reply@example.com'
MAIL_DEBUG = True  # outputs email to console instead of sending them
