# a variation on the Ex16 script that opens and reads the file we created

from sys import argv

script, filename = argv

target = open(filename)

print(target.read())


# print(f"{target}")





