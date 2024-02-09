#A Class is like an object constructor,
#or a "blueprint" for creating objects.

class MyClass:
  x = 5

p1 = MyClass()
#print(p1.x)

class Car:
    model = "Honda"
    wheels = 4
    color = "Red"

    def __init__(self, model, color):
       self.model = model
       self.color = color

    def display__info(self):
       print("My car is a {self.color} {self.model}")

    def change_color(self, color):
       self.color = color

my_car = Car(model="Toyota", color="Blue")
my_car.display__info()
my_car.change_color("White")
my_car.display__info()

#All classes have a function called __init__(),
# which is always executed when the class is being initiated.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ezekiel", 25)

print(p1.name)
print(p1.age)

#The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("Ezekiel", 25)

print(p1)

#Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Ezekiel", 25)
p1.myfunc()

#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Ezekiel", 25)
p1.myfunc()


