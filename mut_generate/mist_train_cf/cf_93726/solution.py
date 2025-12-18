"""
QUESTION:
Implement a class hierarchy using multiple inheritance in Python, where a class 'Bat' inherits properties and methods from both 'Mammal' and 'Flyer' classes, which in turn inherit from a base class 'Animal'. The 'Animal' class should have an initializer method that takes a 'name' parameter, and a 'speak' method that can be overridden by its subclasses.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "I am a mammal."


class Flyer(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "I can fly."


def Bat(name):
    return BatClass(name)


class BatClass(Mammal, Flyer):
    def __init__(self, name):
        super().__init__(name)