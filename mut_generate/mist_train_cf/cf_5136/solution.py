"""
QUESTION:
Write a function named `recursive_sum` that takes in three lists of integers. Implement the function using a recursive approach to compute the sum of all elements in the input lists, achieving a time complexity of O(n), where n is the total number of elements in all three lists combined. Do not use built-in sum functions or loops.
"""

def entance(list_1, list_2, list_3):
    if len(list_1) == 0 and len(list_2) == 0 and len(list_3) == 0:
        return 0
    
    if len(list_1) > 0:
        return list_1[0] + entance(list_1[1:], list_2, list_3)
    
    if len(list_2) > 0:
        return list_2[0] + entance(list_1, list_2[1:], list_3)
    
    if len(list_3) > 0:
        return list_3[0] + entance(list_1, list_2, list_3[1:])