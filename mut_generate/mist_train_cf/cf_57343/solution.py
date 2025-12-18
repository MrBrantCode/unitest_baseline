"""
QUESTION:
Create a function named `compute_mean` that accepts three distinct numerical inputs `a`, `b`, and `c`. The function should return the arithmetic mean of the three inputs. If the inputs are not distinct, the function should print an error message and return `None`.
"""

def compute_mean(a, b, c):
    # Check if the inputs are distinct
    if a == b or a == c or b == c:
        print("Input values should be distinct.")
        return None

    # Compute arithmetic mean
    mean = (a + b + c) / 3

    return mean