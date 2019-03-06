ten_things = "Apples Oranges Crows Bears Beets BattlestarGalactica"
print(f"{ten_things}")

print("There's only 6 things on that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
					"Corn", "Banana", "Girl", "Boy"]
					
while len(stuff) != 10:
	next_one = more_stuff.pop()	# this populates 'more_stuff' 
	print("Adding: ", next_one)		# printing what's being added
	stuff.append(next_one)			# adding
	print(f"There are {len(stuff)} items now.")
	# runs until while condition satisfied, then runs rest of program
	
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])			# index starts at 0, so 1 is Oranges
print(stuff[-1])			# counts backwards in the array
print(stuff.pop())		# hmm so .pop() is last item in the list, it pops it backwards
print(' '.join(stuff))	# remember at beginning, split the list up, this joins it back.
print('#'.join(stuff[3:5]))	#I thought this would join items 3 through 5, but it just joins items 3 and 5