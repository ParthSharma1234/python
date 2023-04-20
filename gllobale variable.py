#Use of global keyword:To access a global variable inside a function there is no need to use global keyword.

# global variable
""" a = 15
b = 10

def add():
	c = a + b
	print(c)

# calling a function
add()"""

#Without global keyword

# Python program showing to modify
# a global value without using global
# keyword

"""a = 15

# function to change a global value
def change():

	# increment value of a by 5
	a = a + 5
	print(a)

change()"""

#With global keyword

"""x = 15
def change():

	# using a global keyword
	global x

	# increment value of a by 5
	x = x + 5
	print("Value of x inside a function :", x)
change()
print("Value of x outside a function :", x)"""
