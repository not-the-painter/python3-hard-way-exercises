# repeat of Ex13 but with one fewer argument variable

# import argv from the sys library
from sys import argv

script, name, pet = argv

print("Hello", name)
print("Your pet's name is", pet)
print("The script is called", script)



