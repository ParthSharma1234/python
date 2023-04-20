#Loops:- Use  to specify a block of code to be
# executed till the specific condition is reached.
#Types of loop in python:-
#1) For Loop:-
#By using list
"""list = ["Parth","Sahil","Ashu","Pratham","Ballu","Prashant"]
for item in list:
    print(item)"""

#Now By using dictionary
"""dictionary1 = {"Seek":1,"Rush":2,"Ambush":3,"Hault":4,"Timithi":5}
for item in dictionary1:
    print(item)
print(type(dictionary1))"""

"""list = [["Parth",1],["Sahil",2],["Harry",3]]
dict1 = dict(list)
print(dict1)
print(type(dict1))
print(type(list))
for item in dict1.items():
    print("items","to and lollypops")"""

"""# We can also use the index of elements in the sequence of iteration i.e. for loop
List = ["geeks","for","geeks"]
for index in range(len(List)):
    print (List[index])

#using else with for loop
List = ["geeks","for","geeks"]
for index in range(len(List)):
    print (List[index])
else:
    print("Inside else block")"""

#2) While Loop:-
"""#EX:-1
i = 0
while(i<30):
    print(i)
    i=i+1

#EX:-2
j = 0
while(j<10):
    print("HELLO")
    j = j+1
    # j = j+2
    # j = j+3
    # j = j+5"""

#EX:-3
i = 10
while i>=0:
    print(i)
    i = i-1#This will print the result in reverse.
    i = i-1+1#Infinite loop 10 will print infinite times.
#NOW we have covered for and while loop but what about do while se the answer is that python
# do net support dowhile loop becoz the object will not be callable coz in do while loop we
# declare the condition later and print the statements before.But if someone wants to use it
# can definately do.