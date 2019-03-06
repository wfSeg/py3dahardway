# Let's go

from sys import exit

def gold_room():		# first function
	print("Room full of gold. How much you going to take?")
	
	choice = input("> ")
	if "0" in choice or "1" in choice:		# so this is kind of arbitrary. What if they type in 999?
		how_much = int(choice)		# changing 'choice' to an integer, assigning it to 'how_much'
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print("Nice guy, not greedy. You win.")
		exit(0)
	else:
		dead("Greedy person. You died.")

def bear_room():		# second function
	print("There's a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False
	
	while True:
		choice = input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear moved from the door.\nYou can go through now.")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed and chews your leg off.")
		elif choice == "open door" and not bear_moved:	# the example didn't have this option
			print("There's kind of a bear in the way.")
			bear_room()
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means.")
			print("try 'take honey', 'taunt bear' or 'open door'")
			
def cthulhu_room():
	print("Whelp, here's Cthulhu")
	print("Do you flee for your life or eat your head?")
	choice = input("> ")
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Game over dude! Game Over.")
	else:
		cthulhu_room()		#ohh nice, this just puts you in an infinite loop until you type the right/wrong thing
		

def dead(why):		#oh, so input from all the 'dead' in above functions, is the 'why' input for this dead functions
	print(why, "Good job~")
	exit(0)
	
def start():
	print("You are in a dark room.\nThere is a door to your right and left.")
	print("Which one do you take?")
	
	choice = input("> ")
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room and starve.")
		
start()	# this starts the whole program