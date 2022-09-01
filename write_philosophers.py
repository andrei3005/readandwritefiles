# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosphers.txt.
    #file_object = open(filename, mode)
    outfile = open('philosophers.txt', 'w')

    #write the names of three philosphers to the file
    # John Locke, David Hume and Edmund Burke
    outfile.write('John Locke' + '\n')
    outfile.write('David Hume' + '\n')
    outfile.write('Edmund Burke' + '\n')

    #close the file
    outfile.close()

# Call the main function.
main()