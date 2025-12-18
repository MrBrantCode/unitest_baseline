"""
QUESTION:
Create a function named `compute_inverse` that takes an integer `n` as input and returns a list of results. The function should calculate the inverse of each number in the range from 0 to `n-1` and append the result to the list. The function should handle `ZeroDivisionError`, `TypeError`, and any other exceptions that may occur during execution. If an exception occurs, the function should print a custom error message and append `None` to the results list.
"""

def compute_inverse(n):
    results = []
    for i in range(n):
        try:
            x = 1/i
            results.append(x)
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            results.append(None)
        except TypeError:
            print("Error: Non-integer value encountered.")
            results.append(None)
        except Exception as e:
            print("Unexpected error: ", str(e))
            results.append(None)
    return results