# accessing list

print("You animals.")
animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

# sooo I'm supposed to write a full sentence following some format.

i = 0

while i < 6:
	#print(f"Hello", animals[i])
	print(f"The animal is at {i} and is a", animals[i])	#no need for 'space' after 'a'
	i = i + 1

i = 5		# need to re-init i, or else will get index out of range
while i > 0:
	print(f"The animal is at {i} and is a", animals[i])
	i = i - 1
	
# hmm how to deal with i value not in list