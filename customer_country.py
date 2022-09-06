import csv

infile = open('customers.csv','r')
outfile = open('customer_country.csv','w')

csvfile = csv.reader(infile,delimiter=',')
#outfile.write("Hi")
next(csvfile)

for record in csvfile:
    #print('Full Name:', record[1], record[2])
    #print("Country:", record[4])
    outfile.write(record[1], record[2])
    #outfile.write(record[4])

outfile.close()