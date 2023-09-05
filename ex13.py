# Passing argument variables to a script using argv
# Remember to pass three argument variables along witht he filename when running this

# import argv from the sys library
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)

