import unittest
from app import app


class BasicTestCase(unittest.TestCase):

    def test_index_route(self):
        """Route Testing for Homepage"""
        indexTest = app.test_client(self)
        response = indexTest.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        """Route Testing for Login Page"""
        loginRoute = app.test_client(self)
        response = loginRoute.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_signup_route(self):
        """Route Testing for Sign Up Page"""
        signupRoute = app.test_client(self)
        response = signupRoute.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
