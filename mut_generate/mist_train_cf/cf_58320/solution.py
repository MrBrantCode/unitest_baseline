"""
QUESTION:
Write a function `get_odds_multiples_and_sort` that takes two lists of integers as input. The function should return a list of integers that are either odd or multiples of 3 from both input lists, combined, sorted in ascending order, and with all numbers greater than or equal to 50 removed.
"""

def get_odds_multiples_and_sort(list1: list, list2: list):
    def is_multiple_of_three(n: int):
        return n % 3 == 0

    odd_and_multiple_numbers = []
    for n in list1 + list2:
        if (n % 2 != 0 or is_multiple_of_three(n)) and n < 50:
            odd_and_multiple_numbers.append(n)

    return sorted(odd_and_multiple_numbers)