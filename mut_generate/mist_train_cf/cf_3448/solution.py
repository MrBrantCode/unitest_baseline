"""
QUESTION:
Create a function `create_animal` that implements the Factory pattern to create different types of animals based on a given `animal_type` parameter. The function should handle at least two animal types ("dog" and "cat") and provide a default case for unrecognized animal types. The function should return an instance of the corresponding animal class, which should have a `speak` method that prints the sound made by the animal.
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class UnknownAnimal(Animal):
    def speak(self):
        print("Unknown animal sound")

def create_animal(animal_type, name):
    """
    Factory function to create different types of animals based on the given animal_type parameter.

    Args:
        animal_type (str): The type of animal to create.
        name (str): The name of the animal.

    Returns:
        An instance of the corresponding animal class.
    """
    if animal_type == "dog":
        return Dog(name)
    elif animal_type == "cat":
        return Cat(name)
    else:
        return UnknownAnimal(name)