# Variation on Ex13 script that combines input() with argv

# import argv from the sys library
from sys import argv

script, name = argv

print("Hello,", name)
age = input("How old are you? ")
print(f"The script {script} now knows you are {age} years old.")

