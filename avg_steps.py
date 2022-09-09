import csv
from functools import total_ordering

infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')

csvfile = csv.reader(infile,delimiter=',')

days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
firstIndex = 0
lastIndex = 0
x = 0
lines = infile.readlines()

outfile.write('Month | Avg Steps\n')
print('Month | Avg Steps\n')

monthNum = 0
    
for num in range(1, 13):
       
    totalSteps = 0
    count = 0
    steps_average = 0
    row = infile.readlines()
     
    for count in range(0, days[monthNum] + 1):
           
        monthRows = row[firstIndex:lastIndex]

        steps_average = float(sum(monthRows)) / max(len(monthRows),1)   #!!!!!
        

       
        print (months[monthNum] + ' | ' + format(steps_average, ',.1f') + ' steps.')
        outfile.write(months[count] + ' | ' + '{0:.1f}'.format(steps_average)+ '\n')
       
        monthNum = monthNum + 1

infile.close()
outfile.close()
