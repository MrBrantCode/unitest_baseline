"""
QUESTION:
Write a function `sum_of_digits(n)` that takes a positive integer `n` as input and returns the sum of its digits, excluding any digits that are divisible by 3. The time complexity of the function should be O(n), where n is the number of digits in the integer.
"""

def entrance(n):
    sum = 0
    num_str = str(n)
    for char in num_str:
        digit = int(char)
        if digit % 3 != 0:
            sum += digit
    return sum