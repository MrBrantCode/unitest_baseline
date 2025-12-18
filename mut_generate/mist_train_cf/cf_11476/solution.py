"""
QUESTION:
Implement a function `sum(a, b)` that adds two numbers and handles two error scenarios: when the inputs are of different data types and when the second input is a list. If the inputs are of different data types but the second input is not a list, the function should return "inputs should be numbers". If the second input is a list, the function should return "second input should not be a list". The function should also print "This function has successfully executed" regardless of the outcome.
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