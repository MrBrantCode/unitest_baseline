"""
QUESTION:
Write a function named `get_unique_elements` that takes a list as input and returns the number of unique elements in the list. The function must have a time complexity of O(n) and cannot use any additional data structures.
"""

def get_unique_elements(lst):
    lst.sort()
    count = 0
    for i in range(len(lst)):
        if i == len(lst) - 1 or lst[i] != lst[i+1]:
            count += 1
    return count