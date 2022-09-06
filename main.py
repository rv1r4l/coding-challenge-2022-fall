# collect data from csv file
# visualize data into graph (model rating vs. time)

import csv
from matplotlib import pyplot as plt
import operator
import pandas as pd

file = open("cars_raw.csv")
type(file)


def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

    return unique_list


csvreader = csv.reader(file)
next(csvreader)
# append index 0, 1, 5 into row to access

rows = []
i = 0
for row in csvreader:
    line = [row[0], row[1], row[5], i]
    rows.append(line)
    i = i + 1
rows
file.close()

models = []

for row in rows:
    for model in row:
        models.append(row[1])

unqModel = unique(models)

rows = sorted(rows, key=operator.itemgetter(0))
rows = sorted(rows, key=operator.itemgetter(1))
switched = True

dev_x = []
dev_y = []
avg = 0
counter = 1
for model in unqModel:
    for row in rows:
        if (model == row[1]):
            dev_x.append(row[0])
            dev_y.append(row[2])






#plt.plot(dev_x, dev_y)
#plt.axis([0,  25, 0, 5])
#plt.show()
