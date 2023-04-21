class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("Delvi", 19)
person1.say_hello()

person2 = Person("Ghina", 20)
person2.say_hello()
