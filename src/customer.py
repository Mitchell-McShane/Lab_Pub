class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_drink(self, drink, wallet):
        wallet = wallet =- drink
        return wallet
