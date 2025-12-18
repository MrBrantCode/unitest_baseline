"""
QUESTION:
Write a function `prefix_decorator` that takes a prefix string as input and returns a decorator function. The decorator function should take a target function as input and return a new function. The new function should print the prefix followed by "Starting..." before calling the target function, and print the prefix followed by "Completed!" after calling the target function. The new function should return the result of the target function.

The function should be a higher-order function that returns a closure. The closure should take the target function as input and return the new function. 

The input prefix should be a string and the target function should be a function with any number of arguments and keyword arguments. The new function should return the result of the target function.
"""

def prefix_decorator(prefix):
    def wrapper_function(original_function):
        def new_function(*args, **kwargs):
            print("{}: Starting...".format(prefix))
            result = original_function(*args, **kwargs)
            print("{}: Completed!".format(prefix))
            return result
        return new_function
    return wrapper_function