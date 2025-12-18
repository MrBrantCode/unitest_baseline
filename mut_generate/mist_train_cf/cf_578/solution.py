"""
QUESTION:
Implement a `count_unique_elements(lst)` function that takes a list of integers as input and returns the count of unique elements. The function should have a time complexity of O(n log n) and use constant space. The input list can contain negative numbers.
"""

def count_unique_elements(lst):
    lst.sort()
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            count += 1
    return count