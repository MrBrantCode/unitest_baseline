"""
QUESTION:
Implement a function `is_higher_order` that takes a single argument `func` and returns `True` if `func` is a higher-order function and `False` otherwise. A higher-order function is a function that takes another function as an argument or returns a function as a result. The function must also be a first-class object. The `is_higher_order` function should be able to handle cases where the input function may not take another function as an argument or may not return a function as a result.
"""

def is_higher_order(func):
    if callable(func):  # Check if the input is a function
        try:
            # Attempt to pass a function as an argument or return a function
            result = func(lambda x: x)  # Pass a lambda function as an argument
            return callable(result)  # Check if the result is a function
        except:
            return False  # If an exception occurs, the function does not satisfy the conditions
    else:
        return False  # If the input is not a function, it does not satisfy the conditions