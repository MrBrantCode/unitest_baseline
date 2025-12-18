"""
QUESTION:
Create a function named `make_sound` that takes an object of the `Animal` class or its subclasses as a parameter and calls the `sound` method of the object. The function should be able to handle objects of different classes without knowing their actual class type. 

The `Animal` class and its subclasses should be implemented such that they have a `sound` method, but with different implementations. The `make_sound` function should be able to work with objects of any class that has a `sound` method, regardless of whether it's an `Animal` object or an object of a subclass of `Animal`.
"""

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_sound(animal):
    return animal.sound()