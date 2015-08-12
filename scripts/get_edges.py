import urllib
import xlrd
import csv
import xml.etree.ElementTree as ET
from   unidecode import *
import xlwt
import sys
import re
import itertools
import networkx as nx

def load_clean(filename):
    soups = []
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        soups.append([row[0], row[1], row[2]])
    return soups
    
edges = load_clean('../processed_data/edges_wo_m.txt')
print len(edges)
print "edges loaded"

G=nx.Graph()
temp =[x for x in edges if x[2] > 1]
G.add_weighted_edges_from(temp)
print "edges added to network"

def load_ed(filename):
    soups = {}
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter=',')
    for row in reader:
        soups[row[0]] = [row[1], row[2:]]
    return soups

small = load_ed('../processed_data/cleaned_editors_small_wo_m.txt')

for node in G:
    if small[node][0] == 'liberal':
        color = -1
    elif small[node][0] == 'science':
        color = 0
    elif small[node][0] == 'conservative':
        color = 1
    else: color = 5
    G.node[node]['color'] = color

print "nodes labelled"

nx.write_graphml(G,'../wom.graphml')

print "done"
