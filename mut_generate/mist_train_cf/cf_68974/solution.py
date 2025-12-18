"""
QUESTION:
Design a function `sum_even_numbers` that takes a list of integers `lst` as input and returns the sum of the even numbers in the list. The function should iterate over the list, identify the even numbers, and calculate their sum.
"""

def sum_even_numbers(lst):
    sum_even = 0
    for i in lst:
        if i % 2 == 0:  # Check if number is even
            sum_even += i
    return sum_even