# import argv from the sys module
from sys import argv

# assign argument variables
script, input_file = argv

# function print_all() takes a file as an argument and prints out the contents
def print_all(f):
	print(f.read())

# function rewind() takes a file as an argument positions the 'cursor' at the beginning with seek(0)
def rewind(f):
	f.seek(0)

# function print_a_line() takes a manually entered line number and a file as arguments
# and prints out the line number and the corresponding line
def print_a_line(line_count, f):
	print(line_count, f.readline())

# assign the file entered on the command line to current_file
current_file = open(input_file)

# print the contents of the file
print("First let's print the whole file:\n")
print_all(current_file)

# 'rewind' the file to the beginning
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

# set current_line to 1 and print the current line in the file
# since we just called rewind() the cursor is at the beginning of the file so the numbers will line up
current_line = 1
print_a_line(current_line, current_file)

# the cursor in readline() advances to the next line automatically, but we have to increment current_line manually
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)