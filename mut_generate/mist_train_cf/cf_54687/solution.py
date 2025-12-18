"""
QUESTION:
Write a function `rearrange_list(lst)` that takes a list of integers `lst` as input. Remove all elements from the list that are divisible by 4, then sort the remaining elements based on two criteria: the count of 1s in their binary representation (primary) and their integer value (secondary). Return the sorted list.
"""

def rearrange_list(lst):
    # Remove all elements divisible by 4
    lst = [i for i in lst if i % 4 != 0]
    # Sort the list based on the count of 1's in their binary representation and their value
    lst.sort(key=lambda x: (bin(x).count('1'), x))
    return lst