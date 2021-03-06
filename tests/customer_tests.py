import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Colin Riddel", 18, 25)
        self.drink = Drink("Jabba Juice", 3, 5)
        self.pub = Pub("Mos Eisley Cantina", 100, "Jabba Juice")

    def test_name(self):
        self.assertEqual("Colin Riddel", self.customer.name)

    def test_wallet(self):
        self.assertEqual(25, self.customer.wallet)

    def test_check_drunkenness(self):
        self.assertEqual(self.customer.drunkenness, self.drink.units)


