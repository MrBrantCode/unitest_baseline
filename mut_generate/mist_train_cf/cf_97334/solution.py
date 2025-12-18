"""
QUESTION:
Write a function `count_positive_integers` that takes a list of integers as input and returns a dictionary where the keys are the positive integers from the list and the values are their respective counts. The function should ignore negative integers and have a time complexity of O(n) and a space complexity of O(n).
"""

def count_positive_integers(lst):
    # Initialize an empty dictionary
    counts = {}

    # Iterate over the list
    for num in lst:
        # Ignore negative integers
        if num <= 0:
            continue

        # Increment the count for the positive integer
        counts[num] = counts.get(num, 0) + 1

    return counts