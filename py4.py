# oh man, can't wait until we get to Classes

cars = 100
space_in_car = 4
drivers = 30
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
ave_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
# you know what I noticed about python compared to php?
# You don't need to add a newline /n to the end of print
# and you don't need to add an extra space " " between strings and variables
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
# I'm using Notepad++, on Windows. But I'm ssh'd into a CentOS server.
# Running all the python scripts on Linux, it's just much easier to setup
# a python environment in Linux. But I like my text editor with a GUI.
# The Mouse is a great moden invention. Don't limit yourself to strictly keyboard.
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", ave_passengers_per_car, "in each car.")

# for exercise question #1, yeah if you use 4, the carpool_capacity will be an integer and not a float
# i.e. 120 vs 120.0