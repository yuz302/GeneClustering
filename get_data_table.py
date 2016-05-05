import os
import csv
import numpy as np

path = '/Users/diana/GitHub/GeneClustering/9a7dd21e-e960-48b8-a734-ea5fce8b41bc/Expression-Genes/UNC__AgilentG4502A_07_3/Level_3'

with open('genes.csv', 'wb') as outfile:
    wr = csv.writer(outfile, delimiter=',',
                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # write first row as sample names
    count = 0
    first_row = ['id']
    for i in range(len(os.listdir(path))-1):
        first_row.append('s'+str(i+1))
    first_row.append('std')
    wr.writerow(first_row)

    ls = os.listdir(path)
    # ignore ds_store
    ls.pop(0)
    first_row.pop(0)
    lss = [x[0:23] for x in ls]
    psn = [lss,first_row]

    # get gene info from the first file
    filename1 = ls.pop(0)
    columns = []
    gene_names = []
    column1 = []
    with open(os.path.join(path, filename1), 'rb') as infile:
        infile.readline()
        infile.readline()
        for row in infile.readlines():
            gene_names.append(row.split()[0])
            column1.append(row.split()[1])

    # add column to columns
    columns.append(gene_names)
    columns.append(column1)

    for filename in ls:
        with open(os.path.join(path, filename), 'rb') as infile:

            infile.readline()
            infile.readline()
            one_file = []

            for row in infile.readlines():
                one_file.append(row.split()[1])
            # add this column to columns
            columns.append(one_file)

    table = zip(*columns)
    for row in table:
        # get the std for each row, add to last column
        last = row[1:]
        dd = []
        for i in last:
            try:
                float(i)
            except:
                continue
            dd.append(float(i))

        standd = np.std(dd)
        sdd = (standd, )
        row = row + sdd
        wr.writerow(row)
        # book.save("genes.xls")

    pair_sample_name = zip(*psn)
    with open('sample_name.csv', 'wb') as outf:
        wr = csv.writer(outf, delimiter='\t',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for rr in pair_sample_name:
            wr.writerow(rr)
