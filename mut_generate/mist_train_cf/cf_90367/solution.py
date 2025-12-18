"""
QUESTION:
Create a function `find_intersection` that takes two lists of integers as input and returns a new list containing the intersection of the two input lists. The input lists can contain duplicates and negative numbers. The function should have a time complexity of O(n), where n is the length of the longer input list, and a space complexity of O(n), where n is the length of the intersection of the two input lists. The input lists should not be modified, and the function should handle empty lists, lists with a single element, and large lists (up to 10^6 elements) efficiently. The resulting list should contain unique elements in the same order as they appear in the first input list.
"""

def find_intersection(list1, list2):
    intersection = []
    if not list1 or not list2:
        return intersection
    
    set1 = set(list1)
    set2 = set(list2)
    
    if len(set1) < len(set2):
        smaller_set = set1
        larger_set = set2
    else:
        smaller_set = set2
        larger_set = set1
    
    for num in smaller_set:
        if num in larger_set:
            intersection.append(num)
    
    return intersection