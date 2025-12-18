"""
QUESTION:
Write a function `my_decorator` that takes a function `func` as an argument and returns a new function that extends the behavior of `func` by printing "Something is happening before the function is called." before calling `func` and "Something is happening after the function is called." after calling `func`. The original function `func` should not be modified.
"""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper