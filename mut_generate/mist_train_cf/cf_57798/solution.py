"""
QUESTION:
Create a function `calculate_permutations` that calculates the total number of permutations of a given string with a specified size. The function should take two parameters: `string` and `size`. The function should return the total number of permutations. Note that the size of the permutations cannot be greater than the length of the input string.
"""

def calculate_permutations(string, size):
    if size > len(string):
        return 0

    length = len(string)
    factorial_length = 1
    for i in range(1, length + 1):
        factorial_length *= i

    factorial_difference = 1
    for i in range(1, length - size + 1):
        factorial_difference *= i

    num_permutations = factorial_length // factorial_difference
    return num_permutations