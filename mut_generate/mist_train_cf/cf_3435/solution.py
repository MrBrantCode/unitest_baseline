"""
QUESTION:
Design a function named `calculate_intersection` that takes two lists as input and returns their intersection. The input lists can contain duplicates and may not be sorted. The resulting intersection list should also contain duplicates if they exist in both input lists. The function should have a time complexity of O(n+m) and a space complexity of O(n+m), where n and m are the lengths of the input lists. The function should also handle the case where one or both input lists are empty.
"""

def calculate_intersection(list1, list2):
    intersection = []
    hash_table = {}
    
    if not list1 or not list2:
        return intersection
    
    for element in list1:
        if element in hash_table:
            hash_table[element] += 1
        else:
            hash_table[element] = 1
    
    for element in list2:
        if element in hash_table and hash_table[element] > 0:
            intersection.append(element)
            hash_table[element] -= 1
    
    return intersection