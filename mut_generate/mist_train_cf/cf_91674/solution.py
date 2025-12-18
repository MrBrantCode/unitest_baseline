"""
QUESTION:
Develop a function `count_and_sum_items` that takes a list of integers as input, where each integer is between 1 and 100 and the list can contain up to 1000 items. The function should return a tuple containing the count of items and the sum of all the items in the list.
"""

def count_and_sum_items(lst):
    count = 0
    total_sum = 0

    for item in lst:
        count += 1
        total_sum += item

    return count, total_sum