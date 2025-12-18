"""
QUESTION:
Create a function named `power` that takes two inputs: `base` and `term`, where `base` can be any number or the string 'e', and `term` is an integer. The function should calculate the value of `base` raised to the power of `term` without using any built-in method or library to calculate exponential values. The function should also handle edge cases such as zero and negative terms. If `base` is 'e', the function should approximate its value to calculate the result.
"""

def power(base, term):
    if term == 0:
        return 1

    if term < 0:
        return 1 / power(base, -term)

    result = 1
    for _ in range(term):
        result *= base

    # in case 'e' is passed as base, approximate its value
    if base == 'e':
        euler_num = 2.718281828459045
        result /= power(euler_num, term)

    return result