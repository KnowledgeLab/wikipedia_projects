import urllib
import xlrd
import csv
import xml.etree.ElementTree as ET
from   unidecode import *
import xlwt
import sys
import re

def load_csv(filename):
    soups = []
    total = 0
    ips = 0
    fil = open(filename, 'rb')
    reader = csv.reader(fil, delimiter='|')
    for row in reader:
        aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",row[1])
        if aa:
            ips = ips + 1
        total = total + 1
    return (ips, total)
    
def main(filename):
	out = open("liberal_ips.txt", 'ab')
	wb = csv.writer(out)
	ips, total = load_csv(filename)
	wb.writerow([ips, total])
	out.close()
    
if __name__ == "__main__":
    main(sys.argv[1])