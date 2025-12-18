"""
QUESTION:
Write a function `reverse_combine_sort` that takes two lists as input, reverses the elements of each list, combines the reversed lists into one, and returns the combined list sorted in ascending order. If either of the input lists is empty, the function should return an empty list.
"""

def reverse_combine_sort(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return []
    else:
        reverse_list1 = list1[::-1]
        reverse_list2 = list2[::-1]
        combined_list = reverse_list1 + reverse_list2
        sorted_list = sorted(combined_list)
        return sorted_list