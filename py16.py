# what can you do with files?
# close: close the file
# read: reads the file
# readline: reads just one line of text
# truncate: Empties the file.. so it's not truncate, it's like Erase
# write('stuff'): Writes into the file
# seek(0): Moves the r/w location to beginning of file.. this is like for HDDs

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("Press CTRL-C to cancel.")
print("Hit RETURN to continue with the script.")

input("?")	#waiting for any button I guess

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")		#yeah it's coming back, I definitely did this years ago
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, close the file.")
target.close()

#coolio, this works. Use exercise 15 script to check it.