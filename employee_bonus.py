import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

for record in csvfile:
    print('ID:', record[0])
    print('Fname:', record[1])
    print('Lname:', record[2])
    salary = float(record[3])
    bonus_percent = float(record[4])
    bonus = salary*bonus_percent
    pay = salary + bonus
    pay_2decimal = "{:.2f}".format(pay)
    print('Pay: '+ '$' + pay_2decimal)
    input()