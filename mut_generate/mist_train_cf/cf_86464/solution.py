"""
QUESTION:
Create a function `remove_duplicates_and_sort` that takes a sorted list of integers in descending order as input and returns a new list with no duplicates, sorted in ascending order, while maintaining the original order of unique elements. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def remove_duplicates_and_sort(lst):
    unique_dict = {}
    for num in lst:
        unique_dict[num] = True

    unique_list = list(unique_dict.keys())
    unique_list.sort()

    return unique_list