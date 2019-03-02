# I'm tired. Should go home now. 
# Yeah going home.
# It's a new day. It's a Friday. But I ain't going home.

print("Practice everything we've covered so far.")
print("You\'d need to know \'bout escapes with \\ that do:")
print('\n newlines and \t tabs.')

poem = """
\tThis is a tab world
with tabs
and newlines \n
yay
no explanation
\n\tit's indented.
"""

print(12 * "-")
print(poem)
print("------------")

def secret(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	

start_point = 10000
beans, jars, crates = secret(start_point)

print("With a starting point of: {} beans".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("Alternative way to do it:")
formula = secret(start_point)
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) #WHOA
