import unittest
from Coin import Coin

class TestCoin (unittest.TestCase):

    def setUp(self):
        self.values = ['heads', 'tails']
        self.test_coin = Coin()

    def test_instance_creation(self):
        """
        Test that the the test_coin object created is indeed an instance of a Coin
        :return:
        """
        self.assertIsInstance(self.test_coin, Coin)

    def test_face_value_init(self):
        self.assertIn(self.test_coin.face, self.values)

    def test_get_face(self):
        self.assertIn(self.test_coin.get_face(), self.values)

    def test_flip(self):
        self.test_coin.flip()
        self.assertIn(self.test_coin.get_face(), self.values)