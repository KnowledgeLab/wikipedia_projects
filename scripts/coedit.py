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
    for row in reader:
        soups.append(row[1])
    return soups
    
def main(filename):
	out = open("science_editors.txt", 'ab')
	wb = csv.writer(out)
	editors = list(set(load_csv(filename)))
	wb.writerow([filename[11:-4]] + editors)
	out.close()
    
if __name__ == "__main__":
    main(sys.argv[1])
