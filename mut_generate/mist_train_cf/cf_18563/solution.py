"""
QUESTION:
Create a function named `remove_duplicates` that takes a list as input and returns a new list with duplicates removed without modifying the original list. The function should not use any built-in Python functions or data structures and should have a time complexity of O(n^2), where n is the length of the input list.
"""

def remove_duplicates(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst