# Dictionary is an unordered collection of items.
# In dictionary we uses key and value.
# This ia the normal way we declare dictionary:-
"""a = {"Parth":"Momos","Sahil":"Paneer","Atharva":"Burger",
      "Ashu":"Pasta","Ballu":"Chole"}
print(a)
print(type(a))
print(a["Parth"])#this will print the value of the key.

# Suppose we want to add something in the list that we forget to add.
b = {"Parth":"Momos","Sahil":"Paneer","Atharva":"Burger",
      "Ashu":"Pasta","Ballu":"Chole"}
b["Prashant"] = "Lollypop"
print(b)

# To delete an element
c = {"Parth":"Momos","Sahil":"Paneer","Atharva":"Burger",
      "Ashu":"Pasta","Ballu":"Chole"}
del c["Sahil"]
print(c)"""

#Functions in dictionary-
#1) Copy:- A shallow copy is being created of that perticular dictionary.
d1 = {"Parth":"Momos","Atharva":"Burger","Ashu":"Pasta","Ballu":"Chole"}
print(d1.copy())
print(d1)

#2)Update:- To update the value in the dictionary.
d2 = {"Parth":"Momos","Atharva":"Burger","Ashu":"Pasta","Ballu":"Chole"}
d2.update({"Atharva":"Pepsi"})
print(d2)

#3)Clear:-
d3 = {"Parth":"Momos","Atharva":"Burger","Ashu":"Pasta","Ballu":"Chole"}
d3.clear()
print(d3)

#4)get:-Return the value of the key.
d4 = {"Parth":"Momos","Atharva":"Burger","Ashu":"Pasta","Ballu":"Chole"}
print(d4.get("Parth"))

#5)Items:-This will return the items present in the list.
d5 = {"Parth":"Momos","Atharva":"Burger","Ashu":"Pasta","Ballu":"Chole"}
print(d5.items())

#6)Values:-This will return the values of the key present in the list.
d6 = {"Parth":"Momos","Atharva":"Burger","Ashu":"Pasta","Ballu":"Chole"}
print(d6.values())