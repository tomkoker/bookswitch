import os
import server
import unittest
import tempfile
import json

from server.models import db, User

class TestConfig:
    DEBUG = True
    TESTING = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "secret"

    # Mail settings

    MAIL_SENDER = 'do-not-reply@example.com'
    MAIL_DEBUG = True  # outputs email to console instead of sending them

class ServerTestCase(unittest.TestCase):

    def setUp(self):

        self.app = server.create_app(TestConfig)

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()


        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()
            db.session.remove()


    def test_not_authenticated(self):
        response = self.client.get('/api/me')
        assert json.loads(response.data.decode('utf-8')) == {'status': 'success',
                                             'data': {'authenticated': False}}

    def test_signup(self):

        data = json.dumps(dict(username='test3',
                               password='test',
                               email='test3@test.com'))

        response = self.client.post('/api/signup',
                                    data=data,
                                    content_type='application/json')
        print(response.data)
        assert 'success' in response.data.decode('utf-8')


    def test_a(self):
        assert True

    def test_b(self):
        assert True

if __name__ == '__main__':
    unittest.main()
