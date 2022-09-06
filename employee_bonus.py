import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')