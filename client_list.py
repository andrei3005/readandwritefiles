def main():

    infile = open('clients.txt','r')

    #number = 0
    #number = 1
    counter = 1

    #line = infile.readline()
    for line in infile:
        #line = infile.readline()
        #number+=1
        #print(str(number) + '. ' + line).rstrip('\n')
        #number+=1

        print(counter,". ",line.rstrip('\n'),sep='')
        counter+=1

main()