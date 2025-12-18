"""
QUESTION:
Implement a function `calculate_area(length, width)` that calculates the area of a rectangle and write a test suite for this function using `pytest` that achieves a minimum code coverage of 90%. Use `mutmut` to perform mutation testing on this function, ensuring that the test suite kills at least 90% of the generated mutations.
"""

def calculate_area(length, width):
    return length * width