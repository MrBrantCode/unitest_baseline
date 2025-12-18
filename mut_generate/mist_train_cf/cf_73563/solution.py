"""
QUESTION:
Write a function named `custom_division` that takes two parameters `a` and `b`. The function should perform floating-point division of `a` by `b` and return the result as an integer if the decimal part is zero; otherwise, return the result as a float.
"""

def custom_division(a, b):
    result = a / b  
    if result.is_integer():  
        return int(result)  
    else:
        return result  