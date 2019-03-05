# meanWHILE

i = 0
numbers = []

while i < 6:
	print(f"At the top i is {i}")
	numbers.append(i)
	
	# you know what, BASH scripting is extremely useful. 
	# They should just teach that instead of O-notation and Al Gore's Rhythm
	# I mean, who needs to dance like the ex-vp?
	
	i = i + 1
	print("Numbers now: ", numbers)
	print(f"At the bottom i is {i}")
	print("The numbers: ")
	
	for num in numbers:
		print(num)