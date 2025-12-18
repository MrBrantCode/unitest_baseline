"""
QUESTION:
Given a long number, return all the possible sum of two digits of it.

For example, `12345`: all possible sum of two digits from that number are:

    [ 1 + 2, 1 + 3, 1 + 4, 1 + 5, 2 + 3, 2 + 4, 2 + 5, 3 + 4, 3 + 5, 4 + 5 ]

Therefore the result must be:

    [ 3, 4, 5, 6, 5, 6, 7, 7, 8, 9 ]
"""

from itertools import combinations

def sum_of_two_digits(num):
    # Convert the number to a string, then map each character to an integer to get the digits
    digits_list = list(map(int, str(num)))
    
    # Generate all combinations of two digits and compute their sums
    sums = [sum(comb) for comb in combinations(digits_list, 2)]
    
    return sums