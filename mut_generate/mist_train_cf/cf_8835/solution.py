"""
QUESTION:
Write a function called `sum_of_even_squares(n)` that calculates the sum of the squares of all even digits in a given positive integer `n`. The function should have a time complexity of O(n), where n is the number of digits in the input number.
"""

def sum_of_even_squares(n):
    total = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            total += int(digit) ** 2
    return total