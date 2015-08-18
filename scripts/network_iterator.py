# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import urllib
import xlrd
import csv
import xml.etree.ElementTree as ET
from   unidecode import *
import xlwt
import sys
import re
import itertools

# <codecell>

def load_clean(filename):
    soups = {}
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        soups[row[0]] = [row[1], row[2:]]
    return soups

# <codecell>

full = load_clean('../processed_data/cleaned_editors_small_wo_active.txt')
print len(full)
# <codecell>

comb = itertools.combinations(full.keys(), 2)
temp = []

i = 0
for tup in comb:
    print i
    i = i + 1
    first = full[tup[0]][1]
    second = full[tup[1]][1]
    weight = len(set(first).intersection(set(second)))
    if weight > 0:
        temp.append((tup[0], tup[1], weight))

# <codecell>

# <codecell>

out = open('../processed_data/edges_wo_active.txt', 'wb')
wb = csv.writer(out)
for item in temp:
    wb.writerow(item)
out.close()
