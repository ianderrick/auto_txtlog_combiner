import os
import socket
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Get the hostname of the computer
hostname = socket.gethostname()

# Format the date and time to include only the numbers, with no special characters
date_string = now.strftime('%Y%m%d')

# Create the output file name
output_file_name = hostname + '_' + date_string + '.txt'

# Get the list of all files in the current directory
files = os.listdir('.')

# Open the output file for writing
output_file = open(output_file_name, 'w')

# Iterate over the files
for file in files:
# Check if the file is a text file
    if file.endswith('.txt'):
# Open the file for reading
        input_file = open(file, 'r')

# Write the file name as a seperator
        output_file.write('\n\n\n' + '-' * 50 + '\n\n')
        output_file.write('FILE: ' + file + '\n\n')
        output_file.write('-' * 50 + '\n\n')

# Read the contents of the file and write them to the output file
        output_file.write(input_file.read())

# Close the input file
        input_file.close()

# Close the output file
output_file.close()
