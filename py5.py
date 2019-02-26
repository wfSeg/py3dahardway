# There are many distractions. Focus. 

print("OK, this is a new one. adding the 'f' in front of the string")
# my_name = "Al Gore" 
my_name = 'Al Gore' 	# keep strings consistent, use single quotes ' ' 
#my_age = "60" 	# oh. this was wrong, that's why got "TypeError: must be str, not int" below for total
my_age = 60
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Red'
my_teeth = 'Yellow'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.") # no 'f' here
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky icky
total = my_age + my_height + my_weight
# getting error.. hmm
print(f"If I add {my_age}, {my_height}, and my {my_weight} I get {total}.")