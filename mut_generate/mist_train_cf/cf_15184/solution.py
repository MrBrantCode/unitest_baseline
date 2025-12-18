"""
QUESTION:
Write a function `merge_lists(list1, list2)` to merge two given lists of equal size into the first list, such that the resulting list contains alternating elements from the two lists. The function should modify the first list in-place without using any additional memory to create a new list. The time complexity of the function should be O(n), where n is the size of the input lists.
"""

def merge_lists(list1, list2):
    n = len(list1)
    for i in range(n):
        list1.insert(2*i+1, list2[i])
    return list1