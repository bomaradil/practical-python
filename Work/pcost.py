# pcost.py
#
# Exercise 1.27
import csv, sys

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

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost: ', cost)