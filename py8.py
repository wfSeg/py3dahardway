formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter, ))
print(formatter.format(
	"I know way too many people here that I didn't know last year, Who the fuck are yall?\n",
	"I swear feels like the last few nights we been everywhere and back\n",
	"But I just cant remember it all, What am I doing, What am I doing,\n",
	"Oh yeah that's right I'm doing me, I'm doing me, I'm livin life right now man\n"
))

# Some Drake came up while doing this