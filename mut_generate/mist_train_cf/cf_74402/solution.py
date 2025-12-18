"""
QUESTION:
Create a function `sayHello` that returns a greeting message with the name of the person. The function should be part of a dictionary with a `name` key, and the message should include the value of the `name` key. The function should use the `this` keyword to access the `name` property of the dictionary. 

Restrictions: The function should be able to correctly access the `name` property of the dictionary using the `this` keyword.
"""

def sayHello(self):
    return f"Hello! My name is {self.name}."