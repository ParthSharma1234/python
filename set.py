s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(3)
s.add(3)
s.add(3)
s.union({1,2,3})
s1=s.intersection({1,2,3,5})
s2=({4,5})
print(s,s1)