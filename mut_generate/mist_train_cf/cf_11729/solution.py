"""
QUESTION:
Write a function `remove_duplicates` that takes a list as input, removes duplicate elements keeping only the first occurrence of each element, and returns the modified list in reverse order.
"""

def remove_duplicates(lst):
    unique_lst = []
    for num in lst:
        if num not in unique_lst:
            unique_lst.append(num)
    return unique_lst[::-1]