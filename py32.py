# Came up out the mud, brush the dirt off of me
# Reading "Introduction to Algorithms" Second Edition
#- Thomas H. Cormen
#- Charles E. Leiserson
#- Ronald L. Rivest
#- Clifford Stein

# It's SO hard getting into it. I get distracted. Sidetracked. Bored.
# Going to Skim through it.
# O notation, Omega notation, Theta notation... riiight. 

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# first loop, goes through list
# also... al gore's rhythms sleepy
for number in the_count:
	print(f"This is count {number}")
	
for fruit in fruits:
	print(f"A fruit of type: {fruit}")
	
#mixed list
for i in change:
	print(f"I got {1}")
	
# building dat wal- er, list
wall = []
# specify range to count to
#for i in range(0, 1000):		#let's not do a 1000
for i in range(0, 6):
	print(f"Adding Brick #{i} to the Wall")
	# now adding it to the list
	wall.append(i)

# showing the wall.. ohboy
for i in wall:
	print(f"Brick #{i} was placed.")