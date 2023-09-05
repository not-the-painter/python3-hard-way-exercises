# more on reading files
# this time we copy the contents of one file to another

from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()

print(f"Does the output file exist? {exists(to_file)}")
print(f"Copying {len(indata)} bytes from {from_file} to {to_file}")

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()

