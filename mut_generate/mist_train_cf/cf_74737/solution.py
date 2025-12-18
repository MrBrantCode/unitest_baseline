"""
QUESTION:
Write a function named `find_mod_max` that accepts a list of numerical inputs, potentially containing non-unique and erroneous values. The function should rectify the errors, then return the number with the most unique digits. If multiple numbers have the same unique digit count, return the number that appears first in the list. Erroneous inputs are considered as non-integer values.
"""

def find_mod_max(numbers):
    mod_max = None
    unique_digit_count = 0
    for num in numbers:
        if not isinstance(num, int):
            continue
        current_unique_digits = len(set(str(abs(num))))
        if current_unique_digits > unique_digit_count:
            unique_digit_count = current_unique_digits
            mod_max = num
    return mod_max