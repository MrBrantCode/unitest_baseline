"""
QUESTION:
Implement a function called `count_positive_integers` that takes a list of integers as input and returns a dictionary where the keys are the positive integers from the list and the values are their respective counts. The function should ignore negative integers in the list, have a time complexity of O(n), and a space complexity of O(n).
"""

def count_positive_integers(lst):
    counts = {}
    for num in lst:
        if num <= 0:
            continue
        counts[num] = counts.get(num, 0) + 1
    return counts