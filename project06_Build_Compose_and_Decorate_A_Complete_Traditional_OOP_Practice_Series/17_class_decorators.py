# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the decorator to Person
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


p = Person("Aliyan")
print(p.greet())
