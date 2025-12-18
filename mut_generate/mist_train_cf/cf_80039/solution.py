"""
QUESTION:
Design a function named `merge_arrays` that accepts two arrays of integers. The function should merge the two arrays, remove all the duplicate elements, and return a new array containing the unique elements sorted in the order from least frequently occurring to most frequently appearing. If the frequency of two elements is the same, it should prioritize the element with the smaller numerical value.
"""

import collections

def merge_arrays(array1, array2):
    # Merge the two arrays
    merged = array1 + array2
    
    # Get frequency of each number
    counter = collections.Counter(merged)
    
    # Sort the numbers by frequency and then value
    sorted_items = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    
    # Return only the numbers from the sorted list of tuples
    return [item[0] for item in sorted_items]