# using read(), write(), truncate(), and close() on text files
# variation on Ex16 to reduce repetition in the code

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

# because we opened the file in write mode the call to truncate() isn't necessary.
	# print("Truncating the file...")
	# target.truncate()				# truncate the file to zero-length

print("Now I'm going to ask you for three lines.")

# Get new lines from user. Assign each line to a variable
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# write the three user-provided lines to the file
target.write(f"{line1} \n{line2} \n{line3}")

# Close the file, let the user know
print("And finally, we close it.")
target.close()

