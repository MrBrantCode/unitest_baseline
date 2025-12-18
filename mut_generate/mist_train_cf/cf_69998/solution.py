"""
QUESTION:
Create a function called `greet(name)` that takes a string `name` as input and returns a greeting based on the name. If the name is "John", the function should return "Welcome!". If the name is "Caroline", the function should return "Goodbye!". For any other name, the function should return "Hello, Guest!".
"""

def entrance(name):  
    if name == "John":
        return "Welcome!"
    elif name == "Caroline":
        return "Goodbye!"
    else:
        return "Hello, Guest!"