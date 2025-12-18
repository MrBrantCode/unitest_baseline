"""
QUESTION:
Write a function `merge_and_sort(list1, list2)` that takes two lists as input and returns a single sorted list containing all elements from both lists in ascending order. The time complexity of the solution should be O(nlogn), where n is the total number of elements in both lists.
"""

def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()  

    return merged_list