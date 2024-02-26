#Inheritance allows us to define a class that
#inherits all the methods and properties from another class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, 
# and then execute the printname method:

x = Person("Alex", "Morgan")
#x.printname()


#Create a class named Student,
# which will inherit the properties
# and methods from the Person class:

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Create an instance of the Student class
x = Student("Alex", "Morgan", 2023)

# Call the welcome method on the instance
x.welcome()
