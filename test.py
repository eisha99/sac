# taken from
# https://stackoverflow.com/questions/20621321/how-to-write-tests-in-python-using-unittest
import os
from app import db
import app
import unittest
import tempfile
from app.db_models import User
from werkzeug.exceptions import HTTPException
# mainly targets routing page

# the class on unit tests was after this assignment was supposed to be submitted, so I do not use coverage here for the sake of time
class KanbanTest(unittest.TestCase):


    def setUp(self):
        """Creates a new test client and initializes a new database"""
        # setup and teardown from documentation
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.app.test_client()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """Closes the test database"""
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    ##

    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    ##

    def signup(self, username, password):
        """Send request to sign up page"""
        return self.app.post('/signup', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_signup_get(self):
        """Test sign up"""
        response = self.app.get('/signup', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_signup_post(self):
        """Test sign up"""
        response = self.signup('admin', '12345678')
        assert b' Kanban board ' in response.data
        user = db.session.query(User).filter(User.username=='admin').first()
        self.assertEqual(user.password, '12345678')
        

    def test_signup_post_duplicate(self):
        """Test if duplicated username is not excepted"""
        self.signup('admin1', '1234567')
        user = db.session.query(User).filter(User.username=='admin1').first()
        self.assertEqual(user.password, '1234567')
        response = self.signup('admin1', '123456')
        assert b'Please, choose a different username. This one is already taken' in response.data
    
    ##

    def login(self, username, password):
        """Send request to login page"""
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_login_get(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_login_page_noerror(self):
        self.signup('admin', '12345678')
        response = self.login('admin', '12345678')
        self.assertEqual(response.status_code, 200)

    def test_login_page_invalid_username(self):
        # invalid pass
        response = self.login('non_existant', '12345678')
        assert b'Invalid username!' in response.data

    def test_login_page_invalid_password(self):
        # invalid pass
        self.signup('admin', '12345678')
        response = self.login('admin', 'wrong')
        assert b'Incorrect password!' in response.data

    ##

    def test_logout(self):
        self.signup('admin', '12345678')
        self.login('admin', '12345678')
        response = self.app.get('/logout', follow_redirects=True)
        # redirects to welcome page
        assert b'Welcome to SAC!' in response.data


if __name__ == '__main__':
    unittest.main()