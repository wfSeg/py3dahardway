# exercise 17

from sys import argv
from os.path import exists 	#well, well, well a new library

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")


in_file = open(from_file)
indata = in_file.read()

# Doing it in one line
#indata = in_file.read(from_file) # nah
#indata = open(from_file).read # nope doesn't work

indata = read(open(from_file)

print(f"The input file is {len(indata)} bytes long")
print(f"Does the output file exists? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")

input()

out_file = open(to_file, 'w')	# what's the 'w' do?
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()