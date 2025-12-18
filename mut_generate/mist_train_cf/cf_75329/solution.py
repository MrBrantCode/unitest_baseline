"""
QUESTION:
Write a function `common_elements(l1, l2, l3)` that takes three lists as input and returns a list of elements that appear in all three lists at the same index. The function should handle lists of different lengths and return common elements up to the length of the shortest list.
"""

def common_elements(l1, l2, l3):
    common = []
    min_len = min(len(l1), len(l2), len(l3))
    
    for i in range(min_len):
        if l1[i] == l2[i] == l3[i]:
            common.append(l1[i])
            
    return common