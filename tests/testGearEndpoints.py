import unittest

from kdm import kdm

class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.app = kdm.app.test_client()

    def tearDown(self):
        pass

    def testGearEndpointExists(self):
        response = self.app.get('/gear')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
