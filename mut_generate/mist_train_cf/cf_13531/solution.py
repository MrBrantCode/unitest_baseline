"""
QUESTION:
Create a function `printOddNumbers` that takes two integers `start` and `end` as input and prints all odd numbers from `start` to `end` (inclusive) using recursion. The function should not print any numbers if `start` is greater than `end`.
"""

def print_odd_numbers(start, end):
    if start > end:
        return
    if start % 2 == 1:
        print(start)
    print_odd_numbers(start + 1, end)