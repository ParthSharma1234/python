#Buildin function:-
# a = 100
# b = 100
# c = sum((a,b))
# print(c)

#Userdefine function:- for that we use def keyword.
#Program for addition
"""def add(a, b):
    sum = a+b
    return sum

num1 = int(input("input 1st number: "))  # input from user for num1
num2 = int(input("input 2nd number:"))  # input from user for num2

print("The sum is", add(num1, num2))  # call te function"""

#Program for average
"""def average(a, b):
  avg = (a+b)/2
  return avg
n1 = int(input("1st no.:-\t"))
n2 = int(input("2nd no.:-\t"))
print("The average is:- \t",average(n1, n2))#average function call
"""

#Nested function:-
def Parth():
    x = 20
def Ballu():
 global x
x = 100
print("Before calling Ballu()",x)
Ballu()
print("After calling Ballu()",x)
Parth()
print(x)