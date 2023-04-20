#Below is the general way in which we can display a list in python.
"""A = ["pen","pencil","notebook","sharpner","eraser"]
print(A)
print(type(A))
"""

#accessing elements of list:-
"""stationarygrocerrylist = ["pen","pencil","notebook","sharpner","eraser"]
numbers = [6,9,1,8,9,3]
print(numbers[5])#o/p will be 3 coz list always starts with 0.
print(type(numbers))"""

#slicing in list
"""numbers = [2,5,7,3,7,0,5]
print(numbers[0:5:2])
print(numbers[::3])
print(type(numbers))"""

#Functions or methods in list:-
#1)length
numbers = [2,5,7,3,7,0,5]
print(len(numbers))

#2)add and remove
numbers = [1,2,3,4,5,6,7,8]
numbers.append(100)#addition
print(numbers)
numbers.remove(5)#removal
print(numbers)
numbers.insert(4,600)#insertion
print(numbers)
#3)min and max
numbers = [1000,3000,40000,50000,7000,3000,15000,130000,300]
print(min(numbers))
print(max(numbers))
#4)change a value
numbers = [100,200,300,400,500,600,700,800]
numbers[2] = 900
print(numbers)

#nested list:- List inside a list.
P = [
    [1,2,3],
    [4,5,6]
     ]
print(P[1][2])

#
x = [2,4]
x += [6,8]
print(x[2]//x[0])

#Addition and multiplication of the list
c = [1,2,3]
print(c + [4,5,6])
print(c * 3)