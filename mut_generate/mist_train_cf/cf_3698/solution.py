"""
QUESTION:
Create a function named `sum` that takes two parameters `a` and `b`. The function should return the sum of `a` and `b` if both are numbers, return a custom error message if both are not numbers, and handle three error scenarios: when one input is a list, when one input is a non-integer number, and when the inputs are different data types. The function should also include a finally block that prints a success message after execution, regardless of whether an error occurred.
"""

def sum(a, b):
    try:
        return a + b
    except TypeError: 
        return "Inputs should be numbers"
    except ValueError:
        return "Inputs should be integers"
    except:
        return "Invalid inputs"
    finally:
        print("This function has successfully executed")