import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Space Waffle", 10, 1)

    def test_name(self):
        self.assertEqual("Space Waffle", self.food.name)

    def test_price(self):
        self.assertEqual(10, self.food.price)

    def test_r_level(self):
        self.assertEqual(1, self.food.r_level)