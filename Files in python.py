#1)Opening of file and perform reading in it, in Python.
"""P = open("fool.txt")
content = P.read()
print(content)
P.close()"""

#2)Readline in file
"""S = open("fool.txt","rt")
print(S.readline())
S.close()"""

#3)Writing in file
"""S = open("fool.txt","w")
S.write("Name:-Parth Sharma")
S.close()"""
"""S = open("fool.txt","a")#This will add the statement in the file
S.write("Name:-Parth Sharma")
S.close()"""

#4)Read a file
"""S = open("fool.txt","r+")#This will add the statement in the file
str = S.read(10);
print = "Read string is:",str
S.close()"""

#5)Rename a file
"""import os
os.rename("fool.txt","Sahil.txt")"""

#6)Delete or remove a file
"""import os
os.remove("delete.txt")#File name that you want to remove"""

#7)tell()method
f = open("Sahil.txt","r")
print(f.readline())
print(f.tell())