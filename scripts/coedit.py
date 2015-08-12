import urllib
import xlrd
import csv
import xml.etree.ElementTree as ET
from   unidecode import *
import xlwt
import sys

def load_csv(filename):
    soups = []
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter='|')
    prev = 0
    for row in reversed(list(reader)):
	curr = int(row[2][1:-7])
	if abs(curr - prev) > 50: 
            soups.append(row[1])
	prev = curr
    return soups
    
def main(filename):
	out = open("../processed_data/liberal_editors_wo_m.txt", 'ab')
	wb = csv.writer(out)
	editors = list(set(load_csv(filename)))
	wb.writerow([filename[11:-4]] + editors)
	out.close()
    
if __name__ == "__main__":
    main(sys.argv[1])
