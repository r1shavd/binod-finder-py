"""
Binod Finder [Python3 version]

The script which filters out the lines in a user specified file where it contains the term "binod".

Author : Rishav Das (https://github.com/rdofficial/)
Created on : April 26, 2021

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 2, 2021

Contributors (If you ever did any changes to this script file, then add up your name and alias below accordingly) :
1. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# Importing the required functions and modules
try:
	from sys import platform
except Exception as e:
	# If there are any errors encountered during the importing of the modules, then we display the error message on the console screen

	print('[ Error : {} ]'.format(e))

# Defining the ANSII color code variables for colored output
if 'linux' in platform:
	# If the operating system type is of linux based, then we define them

	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	red_rev = '\033[07;91m'
	yellow_rev = '\033[07;93m'
	defcol = '\033[00m'
else:
	# If the operating system type is not of linux based, then we define them blank

	red = ''
	green = ''
	yellow = ''
	blue = ''
	red_rev = ''
	yellow_rev = ''
	defcol = ''

def main():
	# DRIVER CODE

	# Displaying the script heading on the console screen
	print(yellow_rev + '[ BINOD - FINDER (PYTHON3) ]' + defcol)
	print()

	# Asking the user for the file location
	filename = input(blue + 'Enter the file location : ' + yellow)
	print(defcol, end = '')

	# Reading the filedate
	content = open(filename, 'r').read()
	content = content.split('\n')

	# Iterating through each lines and checking them
	count = 0
	print(yellow + '\nThe lines which contains the term ' + red + '"binod"' + yellow + ' are listed below : ' + defcol)
	for lineNumber, line in enumerate(content):
		if 'binod' in line.lower():
			# If the line contains the term "binod", then we print the line on the screen

			print('[' + yellow + str(lineNumber + 1) + defcol + '] ' + line)
			count += 1
	if count == 0:
		# If there are no lines found containing the term "binod", then we print the message of not found in the console screen

		print('[' + red + '!' + defcol + '] ' + red + 'No such lines found containing the term ' + yellow + '"binod"' + defcol)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		# If the user pressed CTRL+C key combination, then we quit the script

		quit()
	except Exception as e:
		# If there are any errors encountered during the process, then we display the error on the console screen

		print()
		print(red_rev + '[ Error : {} ]'.format(e) + defcol)
		input('Press enter key to continue...')
