# exercise 15

from sys import argv

script, filename = argv

txt = open(filename)	# this just opens the 'filename' --object--

print(f"Here's your file {filename}:")
print(txt.read())	# this actually 'reads' the --object--

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())