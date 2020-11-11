import unittest
from src.pub import Pub
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Mos Eisley Cantina", 100, ["Jabba Juice", "Spotchka", "Blackroot"])

    
    def test_name(self):
        self.assertEqual("Mos Eisley Cantina", self.pub.name)

    
    def test_till(self):
        self.assertEqual(100, self.pub.till)

    
    def test_drink(self):
        self.assertEqual({
            'name': "Jabba Juice", "units": 5, "price": 3,
            'name': "Spotchka", "units": 10, "price": 5,
            'name': "Blackroot", "units": 3, "price": 2
        }, self.pub.drinks)
    
    
    def test_increase_till(self):
        self.pub.increase_till(5)
        self.assertEqual(105, self.pub.till)
