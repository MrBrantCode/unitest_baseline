"""
QUESTION:
Write a function `sample_method` that takes an initial required argument `arg1`, optional positional arguments `*args`, and an optional keyword argument `arg2` with a default value of `"default"`. The function should handle different types of iterable arguments (lists, tuples, dictionaries) and perform exception handling. Additionally, create a decorator `sample_method_speed_decorator` that measures the execution time of the `sample_method` function. The decorator should also handle any exceptions that occur in the decorated function without stopping program execution.
"""

import time
from functools import wraps

def sample_method_speed_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs): 
       start_time = time.time()

       try:
           result = fn(*args, **kwargs)
       except Exception as e:
           print(f"Error occurred inside function: {e}")
           result = None
           
       end_time = time.time()
       print("Time taken by the function is: ", end_time - start_time)
       return result
       
    return wrapper

@sample_method_speed_decorator
def sample_method(arg1, *args, arg2="default"): 
    for arg in [arg1, *args, arg2]:
        if isinstance(arg, list):
            print(f"List: {arg}")
        elif isinstance(arg, tuple):
            print(f"Tuple: {arg}")
        elif isinstance(arg, dict):
            print(f"Dictionary: {arg}")
        else:
            print(f"Other: {arg}")