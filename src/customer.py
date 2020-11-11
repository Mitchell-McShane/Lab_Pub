class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkenness = 0

    def buy_drink(self, drink, wallet):
        wallet = wallet =- drink
        return wallet

    def check_customer_age(self):
        return self.age >= 18

    def check_drunkenness(self, drink, drunklevel):
        drunklevel = drunklevel =+ drink
        return drunklevel
