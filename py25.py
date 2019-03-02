# I'm on a roll

# This is Function 1
def break_words(stuff):
	"""Breaking up words function"""
	words = stuff.split(' ')
	return words

# so running this just by itself doesn't do anything
# turns out it's part of other functions in this exercise

# This is Function 2
def sort_words(words):
	return sorted(words)
	# this function is kind of redundant, 'sort' is builtin...
	
def print_first_word(words):
	first_word = words.pop(0)
	print(first_word)
	
def print_last_word(words):
	last_word = words.pop(-1)
	print(last_word)
	
def sort_sentence(sentence):
	words = break_words(sentence)	# using Function 2
	return sort_words(words)				# using Function 1
	
def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
# that's a lotta functions for an exercise
# no errors when ran, but no output either