"""
QUESTION:
Create a function `add_lists(list1, list2)` that takes two lists of integers as input and returns a new list containing their element-wise addition. The length of the output list should be equal to the length of the longer input list. If the two input lists have the same length, then the length of the output list should also be the same.
"""

def add_lists(list1, list2):
    max_len = max(len(list1), len(list2))
    result = []
    
    for i in range(max_len):
        sum = 0
        if i < len(list1):
            sum += list1[i]
        if i < len(list2):
            sum += list2[i]
        result.append(sum)
    
    return result