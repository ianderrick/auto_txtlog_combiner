import os
import socket
import datetime

# get the current date and time
now = datetime.datetime.now()

# get the hostname of the computer
hostname = socket.gethostname()

# format the date and time to include only the numbers, with no special characters
date_string = now.strftime('%Y%m%d')

# create the output file name
output_file_name = hostname + '_' + date_string + '.txt'

# get the list of all files in the current directory
files = os.listdir('.')

# open the output file for writing
output_file = open(output_file_name, 'w')

# iterate over the files
for file in files:
    # check if the file is a text file
    if file.endswith('.txt'):
        # open the file for reading
        input_file = open(file, 'r')

        # write the file name as a seperator
        output_file.write('\n\n\n' + '-' * 50 + '\n\n')
        output_file.write('FILE: ' + file + '\n\n')
        output_file.write('-' * 50 + '\n\n')

        # read the contents of the file and write them to the output file
        output_file.write(input_file.read())

        # close the input file
        input_file.close()

# close the output file
output_file.close()
