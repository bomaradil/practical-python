#stock.py
#
#exercise 4.1

class Stock:
    #__slots__ = ('name', 'shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __setattr__(self, name, value):
        if name == 'shares' and not isinstance(value, int):
            raise TypeError(f'This is a {type(value)}')
        if name == 'name' and not isinstance(value, str):
            raise TypeError(f'This is a {type(value)}')
        if name == 'price' and not isinstance(value, float):
            raise TypeError(f'This is a {type(value)}')
        super().__setattr__(name, value)
    def __repr__(self):
        return (f'Stock({self.name}, {self.shares}, {self.price})')
        #return (Stock({self.name}, {self.shares}, {self.price}))
    
    @property
    def cost(self):
        cost = self.shares * self.price
        return cost
    
    def sell(self, shares_to_sell):
        self.shares -= shares_to_sell
        return self.shares

        