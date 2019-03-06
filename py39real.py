# ok, there's actually an exercise for 39

# create mapping of state abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}
	
# create a basice set of states and some cities in them
cities = {
	'CA': 'San Jose',
	'MI': 'Detroit',
	'FL': 'Tempa'
}

# add more cities using another method
cities['NY'] = 'Albany'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)		# a dashed line
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("California's abbreviation is: ", states['California'])
print("New York's abbreviation is: ", states['New York'])

# do it by using state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")	#wait, 'abbrev'? so is .items() the definition for the dict entry?
	
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} hast the city {city}")
	
# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")
	
print('-' *10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
	print("Sorry, no State called \"Texas.\"")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")