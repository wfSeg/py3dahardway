# I go out for boba everyday, sometimes even twice. :|

print("""You enter a dark room with two doors.
Do you go through the door on the LEFT or the door on the RIGHT?""")

choice = input("> ")

#if choice == "L" or "Left":	#hmm capitalization matters. Need a better way to sanitize the input
	# doesn't work.
if choice == "L" or choice == "Left" or choice == "l" or choice == "LEFT":
	print("There is a giant Hillary sitting there.")
	print("What do you do?")
	print("1. Check your emails.")
	print("2. Check her emails.")
	
	hillary = input("> ")
	if hillary == "1":
		print("She ignores you.")
	elif hillary == "2":
		print("She eats your face off.")
	else:
		print(f"Well, doing {hillary} isn't one of the options...")
		print("sicko")
		
#elif choice == "R" or "Right":	# I was going to put in cases for "RIGHT" and "r" too, but it's unecessary
	# doesn't work.
elif choice == "R" or choice == "Right" or choice == "r" or choice == "RIGHT":
	print("There is a giant Trump yelling there.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understanding revolvers yelling melodies.")
		# hahaha, I didn't even read this part when I first coded it. I just replaced door 1 and 2 with L and R
		# then I replaced bear with Hillary, and assumed the other one was another bear.
		# but Trump and Cthullu are kinda interchangeable here, both induce insanity.
		
	insanity = input("> ")
	#if insanity == "1" or "2":	# don't need to specify insanity == "2" again, redundant right?
		# nope. doesn't work.
	if insanity == "1" or insanity == "2":
		print("Your body survives powered by a mind of jello.")
		print("Goo job. Yes, 'Goo' job.")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")

else:
	print("You stumble around and fall on a banana, and pass out. Check your spelling! Capitalizaton matters.")	#the text from the exercise was too morbid.
	
# ok so it didn't work first time around, turns out, you NEED to specify variable for both the booleans