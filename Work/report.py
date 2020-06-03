# report.py
#
# Exercise 2.4

import csv

portfolio = []
#share = {}
def read_portfolio(filename):
    with open(filename) as f:
        next(f)
        for row in csv.reader(f):
            #holding = (row[0], int(row[1]), float(row[2]))
            share = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            portfolio.append(share)
    
    return portfolio

def read_prices(filename):
    with open(filename) as f:
        prices = {}
        for row in csv.reader(f):
           # try:
           #     prices[row[0]] = float(row[1])
           # except IndexError as err:
           #     print('warning empty block', err)
           if row:
               prices[row[0]] = float(row[1])
        return prices
    
def lose