"""
#This is a normal way we declare a string.
a = "Python is a popular programming language.Developed by Guido Von Rousom and released in 1991."
print(a)

#Accessing elements of string.
b = "Python is platform independent."
print(b[0:6])#This is called string slicing.
print(b[0::])
print(b[0:6:2])
"""
#Functions or methods that we use in string:-

#1)to count the no.
d = "How to code in 100 days."
print(len(d))
print(d.count("o"))

#2)ending with
d = "How to code in 100 days."
print(len(d))
print(d.endswith("days."))

#3)lower,upper case, and capitalize
d = "how r u"
print(d.lower())
print(d.upper())
print(d.capitalize())

#4)min and max
x = str(239847239874)
print(min(x))
print(max(x))

#5)find
x = "Parth is a good boy"
print(x.find("is"))#is, is at the 6th position coz in python string always starts with 0.

#6)replace
x = "Atharva is a good boy"
print(x.replace("good","bad"))

#7) alphanumeric

x = "Congratulations you r in hell now"
print(x.isalpha())
y = "Congratulationsyourinhellnow"
print(y.isalpha())
z = "Congratulationsyourinhevennow"
print(z.isalnum())