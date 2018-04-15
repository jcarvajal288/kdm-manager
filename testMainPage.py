import unittest

from kdm import kdm

class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.app = kdm.app.test_client()

    def tearDown(self):
        pass

    def testMainPageUp(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def testMainPageContent(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertTrue('<title>KDM Manager</title>' in response.data.decode())


if __name__ == '__main__':
    unittest.main()
