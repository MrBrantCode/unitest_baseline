"""
QUESTION:
Write a function `count_unique_elements(lst)` that takes a list `lst` as input and returns the number of unique elements in the list, with a time complexity of O(n^2) and without using any additional data structures.
"""

def count_unique_elements(lst):
    count = 0
    for i in range(len(lst)):
        is_unique = True
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                is_unique = False
                break
        if is_unique:
            count += 1
    return count