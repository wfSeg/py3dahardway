# I'ma fix this
# let's run this first, see where the errors are
# pretty easy, run it, find error, fix it, run again, repeat

from sys import argv	# needed this.

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()	# wow got to the end, and go back up here
print("How much do you weigh?", end=' ')	# missing )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv	# ugh argv is annoying, go up to the top, import argv

txt = open(filename)	# ok typo here 'filenme'

print(f"Here's your file {filename}:")	# this needs the (f
print(f"{txt.read()}")	# typo here, 'tx.read'. Also, needs the {} for txt.read, since it's a variable

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(f"{txt_again.read()}")	# .read, {}, and "" added


print('Let\'s practice everything.')		# missing \ break
print('You\'d need to know \'bout escapes\n\twith \\ that do \n newlines and \t tabs.') 	#add in \n\t

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")	# missing "
print(poem)
print("--------------")	# missing "


five = 10 - 2 + 3	# remove leftover -
print(f"This should be five: {five}")	# missing )

def secret_formula(started):	#missing :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100		# missing / operator
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) # add in crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)	# change startpoint to 'start_point'
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30	# typo 'cates'. ALL Done. this is the last error that showed up.
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")	# missing ()

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:		# missing :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:	# missing :
    print("People are less than or equal to dogs.")		# missing "


if people == dogs:		# umm missing =? so it evaluates ==
    print("People are dogs.")

