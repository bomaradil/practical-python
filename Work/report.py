# report.py
#
# Exercise 2.4

import csv

portfolio = []
prices = {}
report = []

def read_portfolio(filename):
    '''
    create a dictionary inside a list from a csv file using a loop 
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            #share = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            share = dict(zip(headers, row))
            portfolio.append(share)
    return portfolio

def read_portfolio_2(filename):
    '''
    create a dictionary inside a list from a csv file using a loop in one line
    '''
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        indices = [ headers.index(colname) for colname in select ]
        portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
    return portfolio

def read_prices(filename):
    '''
    create a list from a csv file
    '''
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
    '''
    comparing the share price with the portfolio price and return if we make a gain or loss
    '''
    total_price = 0
    price_share = 0
    #for i in portfolio:
    total_price = sum([prices[i['name']] * i['shares']] for i in portfolio)
    price_share = sum([i['shares'] * i['price']] for i in portfolio)
        
    if total_price > price_share:
        print('Your losses is: ', round(total_price - price_share, 2))
    else:
        print('your gain is: ', round(price_share - total_price, 2))

def make_report(portfolio, prices):
    '''
    combining the info in the csv portfolio and price file 
    and making a list report for the name, total, price and change of the share 
    '''
    for i in portfolio:
        change = float(prices[i['name']]) - float(i['price'])
        report.append((i['name'], int(i['shares']), prices[i['name']], round(change, 2)))
    return report

def print_report(report):
    '''
    printing the report 
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ----------- ----------- -----------')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$":>6s}{price:<7.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, price_filename):
    '''
    operating the script
    '''
    read_portfolio(portfolio_filename)
    read_prices(price_filename)
    make_report(portfolio, prices)
    print_report(report)

#portfolio = read_portfolio('Data/portfolio.csv')
#prices = read_prices('Data/prices.csv')
#report = make_report(portfolio, prices)
#print_report(report)