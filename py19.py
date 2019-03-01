# You know what I realized, the hardest part learning this years ago was just setting up
# after setting up all the programs and environment, you feel like you accomplished the job
# and then don't really do the learning.

def c_and_c(cheese, box):
	print(f"You have {cheese} cheeses!")
	print(f"You have {box} boxes of crackers!")
	print("Man that's a lot of cheese")
	print("Get a blanket.\n")
	
print("We can just give the function numbers directly:")
c_and_c(20, 30)

print("OR, we can use variable magic:")
amount_cheese = 10
amount_cracker = 50

c_and_c(amount_cheese, amount_cracker) 	#cool, passing variable to the function

print("We can do math inside:")
c_and_c(10 + 20, 5 * 6)

print("And we can combine the two, variables and math:")
c_and_c(amount_cheese + 100, amount_cracker + 1000)

#this is cool and all, but don't mix the 'types'. Once you get strings, int, and floats it gets messy