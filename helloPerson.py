# This is a class declaration. It will allow us to create objects called person
class person:
    # The first function we write will be what is automatically called on object
    # creation. It is used to initialize the data in the object. The values after
    # the equals signs are default values that will automatically fill in any data
    # not provided.
    def __init__(self, title = 'Mr.', firstName = 'John', lastName = 'Doe', age = 42):
        self.title = title
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
    # This method will greet the person by their first name
    def greetInformal(self):
        print("Hello,", self.firstName, "\b!")
        
    # This method will greet the person by their title and last name
    def greetFormal(self):
        print("Hello,", self.title, self.lastName, "\b!")
        
    # This method will tell the person's age
    def howOld(self):
        print(self.firstName, "is", self.age, "years old.")
        
    # This method will tell the person happy birthday and increase their age by 1
    def birthday(self):
        self.age = self.age + 1
        print("Happy Birthday,", self.firstName, "\b! You are now", self.age, "years old.")
        
# By coming back to the left margin, we can start writing the main code. Here
# we will ask the user for information, use that to create a person object, then
# test each method
title = input("What is your title?: ")
firstName = input("What is your first name?: ")
lastName = input("What is your last name?: ")
age = input("How old are you?: ")

# Create the person object
you = person(title, firstName, lastName, int(age))

# Test the methods
you.greetInformal()
you.greetFormal()
you.howOld()
you.birthday()
you.howOld()

# See if you can alter data outside of member functions
you.age = you.age - 1
you.howOld()