class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)#P1 is object of person type

print(p1.name)#person wale class main jaega vaha prr usko name and age miljaega
print(p1.age)
#del p1#to delete the object
print(p1)
p1.age =40 #to modify the age

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
