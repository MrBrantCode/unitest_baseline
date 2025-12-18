"""
QUESTION:
Design a function `compare_lists` that takes two sorted lists as input and returns a list of common elements along with their indices in both lists. The function should handle duplicate elements and return the indices of each occurrence. The lists are sorted in ascending order, and the function should use a two-pointer technique for efficient comparison. The function should return two values: a list of common elements and a list of tuples, where each tuple contains the indices of a common element in both lists.
"""

def compare_lists(list_one, list_two):
    common_elements = []
    indices = []
    i = 0
    j = 0
    
    while i < len(list_one) and j < len(list_two):
        if list_one[i] == list_two[j]:
            common_elements.append(list_one[i])
            indices.append((i, j))
            i += 1
            j += 1
        elif list_one[i] < list_two[j]:
            i += 1
        else:
            j += 1
    
    return common_elements, indices