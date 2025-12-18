"""
QUESTION:
Write a function `greet_person(name)` that takes a string `name` as input, prints out a greeting message with the name, and returns the length of the name without using any built-in functions or libraries.
"""

def greet_person(name):
    print("Hello, " + name)
    length = 0
    for i in name:
        length += 1
    
    return length