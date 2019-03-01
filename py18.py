# Exercise 18

def print_two(*args):
	arg1, arg2 = args
	print("This is the print_two function with *args")
	print("Have to define arg1, arg2 = args")
	print(f"arg1: {arg1}\narg2: {arg2}\n")
	
def print_two_again(arg1, arg2):
	print("This is the print_two_again, don't need to specify args")
	print(f"arg1: {arg1}\narg2: {arg2}\n")
	
def print_one(arg1):
	print("This is print_one function, only one arg")
	print(f"arg1: {arg1}\n")
	
def print_none():
	print("This has no args")
	print("I got nothin'.")
	
print_two("Captain", "Morgan")
print_two_again("Jack", "Sparrow")
print_one("First!")
print_none()

# yay, we're finally getting to functions.
# I feel like college courses probably get these first 20 chapters out in one day