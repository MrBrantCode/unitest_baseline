"""
QUESTION:
Create a function called `find_average` that takes a list of numbers as input and returns the average of the numbers. The function should handle edge cases such as an empty list, division by zero, etc., and should work efficiently even for large inputs.
"""

def find_average(numbers):
    if not numbers:   # This check handles the case when numbers list is empty
        return 0
    
    sum_ = 0  # renamed sum to prevent clashing with built-in Python sum function
    for num in numbers:
        sum_ += num
    
    try:
        return sum_ / len(numbers)
    except ZeroDivisionError:
        return 0