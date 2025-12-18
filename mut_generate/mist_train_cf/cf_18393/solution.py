"""
QUESTION:
Create a higher-order function called "multiplyFunc" that takes two functions, "func1" and "func2", as parameters. The function should return another function that takes two numbers, x and y, applies "func1" to x and "func2" to y, and returns the product of the results. If "func2" attempts to divide by zero, the returned function should catch the ZeroDivisionError and return an error message instead of attempting the multiplication.
"""

def multiplyFunc(func1, func2):
    def multiply(x, y):
        try:
            result1 = func1(x)
            result2 = func2(y)
            return result1 * result2
        except ZeroDivisionError:
            return "Error: Division by zero"
    return multiply