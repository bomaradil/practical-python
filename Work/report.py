# report.py
#
# Exercise 2.4

import csv

portfolio = []
prices = {}
report = []

def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #share = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            share = dict(zip(headers, row))
            portfolio.append(share)
    return portfolio

def read_prices(filename):
    with open(filename) as f:
        
        for row in csv.reader(f):
           # try:
           #     prices[row[0]] = float(row[1])
           # except IndexError as err:
           #     print('warning empty block', err)
           if row:
               prices[row[0]] = float(row[1])
        return prices
        
def loss_gain():
    total_price = 0
    price_share = 0
    for i in portfolio:
        total_price += prices[i['name']] * i['shares']
        price_share += i['shares'] * i['price']
        
    if total_price > price_share:
        print('Your losses is: ', round(total_price - price_share, 2))
    else:
        print('your gain is: ', round(price_share - total_price, 2))

def make_report(portfolio, prices):
    for i in portfolio:
        change = float(prices[i['name']] - i['price'])
        report.append((i['name'], i['shares'], prices[i['name']], round(change, 2)))
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ----------- ----------- -----------')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$":>6s}{price:<7.2f} {change:>10.2f}')

#portfolio = read_portfolio('Data/portfolio.csv')
#prices = read_prices('Data/prices.csv')
#report = make_report(portfolio, prices)
#print_report(report)