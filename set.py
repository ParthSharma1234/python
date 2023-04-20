s = set()#This ia an empty set
s1 =set([1,2,3,4,5])
print(s1)
print(type(s))

#Adding the elements in the set

s = set()
s.add(1)
s.add(2)
s.add(2)
s.add(4)
s.add(4)
s.add(1)
print(s.union({1,2,3,4,5}))#contain all the elements.
print(s.intersection({1,2,4,4,5}))#contain only common elements.
print(s.isdisjoint({1,2,3}))
print(s.issubset({1,2,3}))
print(s.issuperset({1,2,3}))