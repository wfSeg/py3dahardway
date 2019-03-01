# hello fellowkids
# exercise 21

def add(a, b):
	print(f"Adding {a} + {b}")
	return a + b
	
def sub(a, b):
	print(f"Subtracting {a} - {b}")
	return a - b
	
def mult(a, b):
	print(f"Multiplaying {a} * {b}")
	return a * b

def divide(a, b):
	print(f"Dividing {a} / {b}")
	return a / b
	
print("Let's do some math")

age = add(30, 5)
height = sub(90, 22)
weight = mult(35, 10)
#iq = divide(100, 90)	 # don't use this, the floats.. the floats everywhere
iq = divide(1000, 10)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

# Ohhh Extra Credit

print("Here is a puzzle.")

what = add(age, sub(height, mult(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")