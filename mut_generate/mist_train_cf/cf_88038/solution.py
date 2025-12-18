"""
QUESTION:
Create a function called "multiplyFunc" that takes two functions, "func1" and "func2", as parameters and returns another function that takes two numbers, x and y. This returned function should apply "func1" to x and "func2" to y, then multiply the results and return the product. However, if "func2" attempts to divide by zero, the returned function should raise a custom exception instead of attempting the multiplication.
"""

def multiplyFunc(func1, func2):
    def multiply(x, y):
        result1 = func1(x)
        try:
            result2 = func2(y)
            return result1 * result2
        except ZeroDivisionError:
            raise Exception("Division by zero is not allowed!")
    return multiply