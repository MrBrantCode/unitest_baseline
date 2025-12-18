"""
QUESTION:
Create a function named `bottleneck` that takes a list of integers as input and returns the index of the "bottleneck" element. A bottleneck element is defined as an element where the sum of all elements to the left is equal to the product of the elements to the right. If no such element exists, return -1.
"""

def bottleneck(lst):
    for i in range(1, len(lst)-1):
        if sum(lst[:i]) == 1 or sum(lst[:i]) == -1:  
            continue
        elif sum(lst[:i]) == 0:  
            if sum(lst[i+1:]) == 0:
                return i
        else:
            product = 1
            for j in lst[i+1:]:
                product *= j
            if sum(lst[:i]) == product:
                return i
    return -1