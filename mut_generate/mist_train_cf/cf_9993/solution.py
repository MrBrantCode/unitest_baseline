"""
QUESTION:
Implement a function called `find_single_occurrence_index(arr)` that finds the index of the element that occurs only once in the given array `arr`. The function should not use any built-in functions or libraries other than basic data structures and algorithms provided by the programming language. The input array `arr` contains at least one element that occurs only once.
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