"""
QUESTION:
Write a function named `multiply` that takes two numbers as arguments, returns their product, and uses a closure for encapsulation. Implement this function in ES5 syntax. When called with arguments 2 and 3, it should return a function that, when invoked, returns the product of 2 and 3.
"""

def multiply(x, y):
    def product():
        return x * y
    return product