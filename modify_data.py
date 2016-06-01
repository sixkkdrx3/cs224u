import os
import utils
import numpy as np

f = open('uniform_data.csv', 'r')
ff = open('data.csv', 'w')

for line in f:
    args = line.split(',')
    k = int(args[0])
    new_category = None
    if k < 3:
        new_category = str(k)
    elif k < 6:
        new_category = str(k-1)
    elif k < 11:
        new_category = str(k-2)
    else:
        new_category = '9'
    args[0] = new_category
    ff.write(','.join(args))
