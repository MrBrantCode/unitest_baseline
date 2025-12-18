"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of strings as input and returns the list with all duplicates removed while maintaining the original order of the elements. The function should have a time complexity of O(n^2) and a space complexity of O(1), without using any built-in functions or methods that directly remove duplicates or additional data structures.
"""

def remove_duplicates(lst):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                lst.pop(j)
            else:
                j += 1
        i += 1
    return lst