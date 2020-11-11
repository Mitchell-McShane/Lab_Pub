import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Jabba Juice", 3)

    def test_name(self):
        self.assertEqual("Jabba Juice", self.drink.name)

    def test_price(self):
        self.assertEqual(3, self.drink.price)