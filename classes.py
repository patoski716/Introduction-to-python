# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object
#Create class
class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greetings(self):
        return f'My name is {self.name} and I am {self.age} year old'

    def has_birthday(self):
        self.age +=1
#  Init user object
pato = User('Patrick Chukwudifu', 'patoski716@gmail.com', 29)
# print(pato.name)

pato.has_birthday()
num=pato.greetings()
print(num)
