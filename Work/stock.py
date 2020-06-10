#

class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)

    def cost(self):
        cost = self.shares * self.price
        return cost
    
    def sell(self, shares_to_sell):
        self.shares -= shares_to_sell
        return self.shares

        