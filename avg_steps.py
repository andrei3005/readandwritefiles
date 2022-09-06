import csv

infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

outfile.write("Month, Avg Steps\n")
for record in csvfile:
    if record[0] == "1":
        month = "January"
        steps = record[2]