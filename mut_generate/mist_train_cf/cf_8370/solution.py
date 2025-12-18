"""
QUESTION:
Write a function `find_intersection(list1, list2)` that takes two lists of integers as input and returns a new list containing the intersection of the two input lists. The function should have a time complexity of O(n), where n is the length of the longer input list, and a space complexity of O(n), where n is the length of the intersection of the two input lists. The input lists should not be modified, and the function should handle empty lists, lists with a single element, and lists with a large number of elements efficiently. The elements in the resulting list should be in the same order as they appear in the first input list, and the resulting list should not contain any duplicate elements.
"""

def find_intersection(list1, list2):
    if not list1 or not list2:
        return []
    
    set1 = set(list1)
    set2 = set(list2)
    
    if len(set1) < len(set2):
        smaller_set = set1
        larger_set = set2
    else:
        smaller_set = set2
        larger_set = set1
    
    intersection = [num for num in smaller_set if num in larger_set]
    
    return intersection