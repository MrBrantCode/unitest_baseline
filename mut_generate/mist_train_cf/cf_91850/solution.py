"""
QUESTION:
Implement a function `sum(a, b)` that takes two inputs `a` and `b` and returns their sum. The function should handle two error scenarios: 
- When `a` and `b` are of different data types that cannot be added together, return "inputs should be numbers".
- When `b` is a list, return "second input should not be a list".
Additionally, the function should print "This function has successfully executed" regardless of whether an error occurred or not.
"""

def sum(a, b):
    try:
        return a + b
    except TypeError as e:
        if isinstance(b, list):
            return "second input should not be a list"
        else:
            return "inputs should be numbers"
    finally:
        print("This function has successfully executed")