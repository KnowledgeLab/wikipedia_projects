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

full = load_clean('../processed_data/cleaned_editors_full.txt')

# <codecell>

comb = itertools.combinations(full.keys(), 2)
temp = []

for tup in comb:
    first = full[tup[0]][1]
    second = full[tup[1]][1]
    weight = len(set(first).intersection(set(second)))
    if weight > 0:
        temp.append((tup[0], tup[1], weight))

# <codecell>

len(temp)

# <codecell>


