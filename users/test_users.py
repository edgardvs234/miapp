import unittest
import views
import models

class TestWebService(unittest.TestCase):
    def test_login(self):
        response= views.login

        self.assertEqual(response, "El usuario existe")
