"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of integers as input, removes duplicates and negative numbers, and returns the distinct positive values in descending order. The function should have a time complexity of less than O(n^2), where n is the size of the input list.
"""

def remove_duplicates(numbers):
    distinct_values = set()

    for num in numbers:
        if num > 0:
            distinct_values.add(num)

    distinct_list = list(distinct_values)
    distinct_list.sort(reverse=True)

    return distinct_list