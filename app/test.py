import unittest

from server import app


class TestPost(unittest.TestCase):
    def test_get(self):

        self.test_app = app.test_client()

        response = self.test_app.get('/', content_type='html/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
