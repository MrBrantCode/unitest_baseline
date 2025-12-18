"""
QUESTION:
Given two positive integers a and b, create a function named `generate_integers` that takes a and b as parameters and returns a vector containing the unique even numerical digits found within the range between a and b, in ascending order. The function should handle cases where a is greater than b, and it should return an empty vector if no even digits are found in the range.
"""

def generate_integers(a, b):
    # use a set to guarantee the unique and ascending order of numbers
    result_set = set()
    lower = min(a, b)
    upper = max(a, b)
    for i in range(lower, upper + 1):
        num = i
        # extracting the digits and checking whether it is an even number less than 10 or not
        while num > 0:
            digit = num % 10
            num //= 10
            if digit % 2 == 0 and digit < 10:
                result_set.add(digit)
    # converting the set to a list and sorting it
    result = sorted(list(result_set))
    return result