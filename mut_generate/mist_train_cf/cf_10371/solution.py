"""
QUESTION:
Write a function to demonstrate multiple inheritance using two base classes: Animal and Flyer, where Animal has methods 'eat' and 'sleep', and Flyer has methods 'take_off', 'fly', and 'land'. The function should allow for the creation of two derived classes, Bird and Bat, that inherit from both Animal and Flyer, and enable access to methods from both base classes.
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Flyer:
    def __init__(self, name):
        self.name = name
    
    def take_off(self):
        print(f"{self.name} is taking off.")

    def fly(self):
        print(f"{self.name} is flying.")

    def land(self):
        print(f"{self.name} is landing.")


def create_derived_class(name, base_class1, base_class2):
    return type(name, (base_class1, base_class2), {})


Bird = create_derived_class("Bird", Animal, Flyer)
Bat = create_derived_class("Bat", Animal, Flyer)