# pcost.py
#
# Exercise 1.27
import csv, sys
from sys import argv
from fileparse import parse_csv

def portfolio_cost(filename):
    with open(filename) as f:
        headers = next(f)
        cost = 0

        for lineno, line in enumerate(csv.reader(f), start=1):
            #line = line.split(',')
            _record = dict(zip(headers, line))
            try:
                cost += float(line[-1]) * int(line[-2])
            except ValueError as err:
                print(f'Warning : Line {lineno}: Bad line: {line}: ', err)
        
    return cost

def portfolio_cost2(filename):
    cost = 0
    for i in parse_csv(filename, select=['shares', 'price'], types=[int, float]):
        cost += i['price'] * i['shares']
    return cost

def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost2(filename)
    print('Total cost: ', cost)

if __name__ == '__main__':
    main(sys.argv)
    
