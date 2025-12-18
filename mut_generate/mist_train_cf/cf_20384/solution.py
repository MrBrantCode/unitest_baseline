"""
QUESTION:
Create a function called `add` that takes two parameters and returns their sum. Implement function overloading to allow the function to accept either two integers, two doubles, or two strings. Then, create a parent class called `Animal` with a method called `sound` and a child class called `Dog` that overrides the `sound` method. The `sound` method in the child class should return "The dog barks".
"""

def add(a, b):
    """
    This function takes two parameters and returns their sum.
    It implements function overloading to allow the function to accept either two integers, two floats, or two strings.

    Parameters:
    a (int or float or str): The first number or string.
    b (int or float or str): The second number or string.

    Returns:
    int or float or str: The sum of a and b.
    """
    return a + b


class Animal:
    """
    This is a parent class with a method called sound.
    """

    def sound(self):
        """
        This method returns a string representing the sound of the animal.
        """
        pass


class Dog(Animal):
    """
    This is a child class that overrides the sound method.
    """

    def sound(self):
        """
        This method returns "The dog barks".
        """
        return "The dog barks"