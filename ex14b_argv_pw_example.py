from sys import argv
import os

filename, PWD = argv

if PWD != '12345':
	print("Wrong password. Exiting.")
	exit()
else:
	print("The script is called:", filename)
	print("You can find it in:", os.getcwd())

exit()
