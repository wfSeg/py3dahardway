# Exercise 23: Strings, Bytes, and Character Encodings

import sys
script, encode, errors = sys.argv


def main(lang_file, encode, errors):
	line = lang_file.readline()
	
	if line:
		print_line(line, encode, errors)
		return main(lang_file, encode, errors)
		
def print_line(line, encode, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encode, errors=errors)
	cooked_string = raw_bytes.decode(encode, errors=errors)
	
	print(raw_bytes, "<===>", cooked_string)
	
	
languages = open("languages.txt", encoding="utf-8")

main(languages, encode, errors)

# To run this, need to do 
# python py23.py utf-8 strict <-- need two extra command line arguments
# try it with utf-16 and big5