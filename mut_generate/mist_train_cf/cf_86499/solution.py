"""
QUESTION:
Implement a function `count_unique_elements()` that takes a list of integers as input and returns the count of unique elements. The function must have a time complexity of O(n log n) and use constant space, without any additional data structures such as sets or dictionaries. The input list may contain negative numbers, which must be handled correctly.
"""

def count_unique_elements(lst):
    lst.sort()
    count = 1
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            count += 1
    return count