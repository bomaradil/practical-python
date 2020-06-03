# pcost.py
#
# Exercise 1.27
import csv, sys

def portfolio(filename):
    with open(filename) as f:
        next(f)
        cost = 0
        
        for line in csv.reader(f):
            #line = line.split(',')
            try:
                cost += float(line[-1]) * int(line[-2])
            except ValueError as err:
                print('Warning :', err)
        
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio(filename)
print('Total cost: ', cost)