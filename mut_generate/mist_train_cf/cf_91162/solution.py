"""
QUESTION:
Find the index of the element that occurs only once in the array without using any built-in functions or libraries. The function should be named `find_single_occurrence_index` and it should take an array as input. The array contains only integers and has at least one element that occurs only once.
"""

def find_single_occurrence_index(arr):
    counts = {}  # empty hash table
    
    # counting occurrences of each element
    for element in arr:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
    
    # finding the element with a count of 1
    for i in range(len(arr)):
        if counts[arr[i]] == 1:
            return i