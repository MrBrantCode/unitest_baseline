"""
QUESTION:
Write a Python function `second_largest` that takes a list of numerical elements as input and returns the penultimate highest value. If the input list has less than two elements, the function should return without a value.
"""

def second_largest(numbers):
    # In case the list has less than 2 elements
    if len(numbers)<2:
        return
    first=max(numbers)
    numbers.remove(first)
    second=max(numbers)
    return second