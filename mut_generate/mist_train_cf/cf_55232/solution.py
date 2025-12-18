"""
QUESTION:
Create a function called get_median that takes a two-dimensional list of integers or floating-point numbers as input. The function should calculate and return the median of all numbers in the list, ignoring empty sub-lists. The function should handle cases where the total number of elements is odd or even, and return None if the input list contains no numbers.
"""

def get_median(lst):
    numbers = [n for sublist in lst for n in sublist if sublist]
    numbers.sort()
    length = len(numbers)
    if length == 0:
        return None
    if length % 2 == 0:
        # Average of two middle numbers
        return (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    else:
        # Middle number
        return numbers[length // 2]