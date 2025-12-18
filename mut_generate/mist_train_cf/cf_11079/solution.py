"""
QUESTION:
Write a function `count_and_sum_items(lst)` that takes a list of up to 1000 positive integers between 1 and 100 as input, and returns a tuple containing the count of items and their sum.
"""

def count_and_sum_items(lst):
    count = 0
    total_sum = 0

    for item in lst:
        count += 1
        total_sum += item

    return count, total_sum