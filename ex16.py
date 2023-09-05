# using read(), write(), truncate(), and close() on text files

# import argv from sys
from sys import argv

script, filename = argv

# warn the user that the file will be erased
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")	# option to escape and keep the file intact
print("If you do what that, hit RETURN.")			# or commit to the erase
input("? ")

print("Opening the file...")
target = open(filename, 'w')	# open the file and assign its contents to the file object 'target'

print("Truncating the file...")
target.truncate()				# truncate the file to zero-length

print("Now I'm going to ask you for three lines.")

# Get new lines from user. Assign each line to a variable
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write the three user-provided lines to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Close the file, let the user know
print("And finally, we close it.")
target.close()

