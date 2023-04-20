#1)Local:-
"""def func():
    x = 300
    print(x)
func()"""

#2)Global:-
"""x = 300
def func():
    print(x)
func()
print(x)"""

#3)Global keyword:-
"""#this is a global variable
a = 100
b = 100
def add():
    c = a+b
    print(c)
add()#calling the function"""

#Now without global keyword
"""a = 15
def change():
    a = a+5
print(a)
change()"""
#Without global it will throw an error so we have to include global keyword.

a = 15
def change():
    global a
    a = a+5
print(a)
change()