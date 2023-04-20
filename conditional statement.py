#1) If else Statement:-
"""A = 456
B = 123
C = int(input())

if B<C:
    print("B is less than C")
if B>C:
    print("B is greater than C")
else:
    print("B is equal to C")"""

#2) Else if(elif):-
"""A = int(input())
B = int(input())
C = 100

if A > B:
    print("A is greater than B")
elif A == C:
    print("A and C are equal")
else:
    print("A is less than B")"""

#3) List in if else
#Scenario 1:-
"""List1 = [1,2,3,4,5]
if 100 in List1:
    print("Yes it is available!")
else:
    print("Not available!")

#print(List1)
#print(type(List1))"""

#Scenario 2:- we use boolean in the list as well.
list1 = [5,7,3]
print(2 in list1)#boolean statement
if 5 in list1:
    print("YES!")
if 1 not in list1:
    print("NO!")