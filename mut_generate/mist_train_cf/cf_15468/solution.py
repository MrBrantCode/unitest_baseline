"""
QUESTION:
Create a function called 'merge_and_sort' that takes two lists as input, 'list1' and 'list2'. The function should return a new list containing the elements of both lists in ascending order, with no duplicates, and without any negative numbers. The elements from 'list1' should come before any element from 'list2' in the new list, but this condition will be satisfied if the resulting list is sorted. The length of the new list should be equal to the sum of the lengths of 'list1' and 'list2' after removing duplicates and negative numbers.
"""

def merge_and_sort(list1, list2):
    combined_list = list1 + list2
    combined_list = sorted(set(combined_list))
    return [x for x in combined_list if x >= 0]