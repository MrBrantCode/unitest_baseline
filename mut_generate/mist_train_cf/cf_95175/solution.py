"""
QUESTION:
Create a higher-order function called "multiplyFunc" that takes two functions, "func1" and "func2", as parameters and returns a function that takes two numbers, x and y. This returned function should apply "func1" to x and "func2" to y, then multiply the results and return the product. However, if "func2" attempts to divide by zero, the returned function should catch the error and return an error message instead.
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