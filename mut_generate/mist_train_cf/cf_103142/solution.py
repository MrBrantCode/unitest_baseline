"""
QUESTION:
Create a higher-order function called "multiplyFunc" that takes two functions, "func1" and "func2", as parameters. The "multiplyFunc" function should return another function that takes two numbers, x and y, and applies "func1" to x and "func2" to y before multiplying the results and returning the final product. The returned function should not take any additional parameters other than x and y.
"""

def multiplyFunc(func1, func2):
    def func(x, y):
        return func1(x) * func2(y)
    return func