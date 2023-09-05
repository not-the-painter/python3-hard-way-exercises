# reading text from files

# import argv from the sys library
from sys import argv

# define script and filename as argument variables.
# These are the values that are passed to the interpreter 
# when we run the script from the command line
script, filename = argv

txt = open(filename)	# open the file in the filename argv variable and assign it to txt
prompt = "> "			#purely cosmetic, assigns a text string to the prompt variable in input()

print(f"Here's your file {filename}: \n")	# format string to display the filename
print(txt.read())		# print the contents of txt
txt.close()

#  more of the same...
print("Type the filename again: ")
file_again = input(prompt)
txt_again = open(file_again)

print(txt_again.read())
txt_again.close()


