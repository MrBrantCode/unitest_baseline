"""
QUESTION:
Write a function `find_armstrong_numbers` that takes two parameters, `start` and `end`, which define the numerical interval. The function should return a list of Armstrong numbers within the given interval, where an Armstrong number is defined as a number that equals the sum of its own digits each raised to the power of the number of digits.
"""

def find_armstrong_numbers(start, end):
    """
    Returns a list of Armstrong numbers within the given interval.

    Args:
        start (int): The start of the numerical interval.
        end (int): The end of the numerical interval.

    Returns:
        list: A list of Armstrong numbers.
    """
    armstrong_numbers = []
    for num in range(start, end + 1):
        digits = list(str(num))
        sum_cubes = sum([int(digit)**len(digits) for digit in digits])
        if sum_cubes == num:
            armstrong_numbers.append(num)
    return armstrong_numbers