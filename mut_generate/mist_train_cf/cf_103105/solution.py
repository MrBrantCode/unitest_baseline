"""
QUESTION:
Write a function `sum_even_integers` that takes a list of integers as input and returns a tuple containing the sum and count of even integers in the list that are greater than 10 and less than 100. If no such integers exist, return 0.
"""

def sum_even_integers(lst):
    count = 0
    total = 0
    for num in lst:
        if num > 10 and num < 100 and num % 2 == 0:
            count += 1
            total += num
    return total, count