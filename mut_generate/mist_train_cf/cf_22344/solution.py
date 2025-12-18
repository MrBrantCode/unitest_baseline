"""
QUESTION:
Create a function named `merge_and_sort` that takes two lists `list1` and `list2` as input and returns a single sorted list containing all elements from both lists in ascending order. The function should have a time complexity of O(nlogn), where n is the total number of elements in both lists.
"""

def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()  

    return merged_list