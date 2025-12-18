"""
QUESTION:
Write a function `find_first_non_repeating_element` that takes an array of integers as input and returns the first non-repeating element in the array. The function should handle arrays containing both positive and negative integers, as well as duplicate elements. If no non-repeating elements exist in the array, the function should return `None`.
"""

def find_first_non_repeating_element(array):
    count = {}
    
    for num in array:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    
    for key, value in count.items():
        if value == 1:
            return key
    
    return None