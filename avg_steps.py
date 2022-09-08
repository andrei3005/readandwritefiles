import csv
from functools import total_ordering

infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

steps = 0
steps_total = 0
amount = 0
total = 0
steps_average = 0
steps_avg_2decimal = 0
days = 31

outfile.write("Month, Avg Steps\n")
for record in csvfile:
    if record[0] == "1":
        month = "January"
        steps = float(record[1])
        steps_total += steps
        amount = float(record[0])
        total += amount
        steps_average = steps_total/total
        steps_avg_2decimal = "{:.2f}".format(steps_average)
        #print(month, ',', steps_avg_2decimal)
    
    #elif record [0] == "2":
        #month = "February"
        #steps = float(record[1])
        #steps_total += steps
        #feb_steps_average = steps_total/days
        #feb_steps_avg_2decimal = "{:.2f}".format(feb_steps_average)
        #print(month, ',', feb_steps_avg_2decimal)

#print(month, ',', steps_avg_2decimal)

#print(total)
#print(steps_average)
print(month, ',', steps_avg_2decimal)
