"""
QUESTION:
Create a function `rearrange_array(arr)` that takes an array of integers as input, rearranges the array such that all elements divisible by 4 appear first while maintaining their original relative order, followed by the remaining elements in their original relative order.
"""

def rearrange_array(arr):
    output = []
    
    # Traverse through the input array
    for element in arr:
        if element % 4 == 0:
            output.append(element)
    
    # Traverse through the input array again
    for element in arr:
        if element % 4 != 0:
            output.append(element)
    
    return output