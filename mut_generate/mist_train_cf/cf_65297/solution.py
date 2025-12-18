"""
QUESTION:
Create a decorator function named `my_decorator` in Python that takes a function as an argument and returns a new function that prints "This is before the function execution." before and "This is after the function execution." after the execution of the original function. Apply this decorator to a function named `my_function` that prints "This is inside the function." The decorator should not take any arguments other than the function to be decorated.
"""

def entrance(func):
    def inner():
        print("This is before the function execution.")
        func()
        print("This is after the function execution.")
    return inner