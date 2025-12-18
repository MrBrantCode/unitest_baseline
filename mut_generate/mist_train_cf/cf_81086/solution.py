"""
QUESTION:
Create a function called 'Meta' that controls the creation of classes, allowing you to add a new attribute to the class with a value of 100, where the attribute name is the lowercased class name. This function should be a metaclass that can be used to create multiple classes with the specified behavior.
"""

def Meta(name, bases, attrs):
    attrs[name.lower()] = 100  # add a new attribute to the class
    return type(name, bases, attrs)