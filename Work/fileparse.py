# fileparse.py
#
# Exercise 3.3

import csv



def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    parse a csv file into a list of records
    '''
    if select and has_headers == False:  
        # raising an expection if select=true and has_headers=False
        raise RuntimeError("select arguement requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []

        if has_headers:     # if the csv file has a headers
            headers = next(rows)  # read the file headers

            if select:  # if a colum select was given
                # making sure that elements in select exit in the headers
                for c in range(len(select)):
                    if select[c] in headers:
                        continue
                    else:
                        print('select element are not in the headers of csv file')
                        break
            # mapping the colum selection to indices
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []

            for lineno, row in enumerate(rows, start=1):
                if not row:  # skip empty lines
                    continue
                if indices:  # filter the row if specific colums were selected
                    row = [row[index] for index in indices]
                    
                if types:  # marking the type of values
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as err:
                        if silence_errors == False:
                            print(f'row {lineno}: couldn\'t convert {row}')
                            print(f'row {lineno}: {err}')
                            continue
                        else:
                            continue
                        
                record = dict(zip(headers, row))
                records.append(record)

        else:
            # if no headers in the csv file
            for row in rows:
                if not row:  # skip empty lines
                    continue
                if types:  # marking the type of values
                    row = [func(val) for func, val in zip(types, row)]

                record = (row[0], row[1])
                records.append(record)

        return records
