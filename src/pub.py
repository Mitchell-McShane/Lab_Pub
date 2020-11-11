class Pub:
    def __init__(self, name, till, stock):
        self.name = name
        self.till = till
        self.drinks = {
        'name': "Jabba Juice", "units": 5, "price": 3,
        'name': "Spotchka", "units": 10, "price": 5,
        'name': "Blackroot", "units": 3, "price": 2
        }
        self.stock = self.drinks

    def increase_till(self, amount):
        self.till += amount
