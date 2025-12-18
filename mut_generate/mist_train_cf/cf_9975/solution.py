"""
QUESTION:
Write a function named `count_equal_elements` that takes an array as input and returns the count of elements next to each other that are equal. The function should handle cases where the input array is empty or contains only one element.
"""

def count_equal_elements(a):
    if len(a) < 2:  
        return 0
    count = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count += 1
    return count