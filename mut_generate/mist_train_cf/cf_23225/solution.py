"""
QUESTION:
Implement a function named `linearSearch` that performs a linear search on a sorted array in ascending order. The function should take two parameters: the sorted array (`sortedArray`) and the target element to search for (`target`). It should return the index of the target element if found, and -1 otherwise.
"""

def linearSearch(sortedArray, target):
    found = False
    for i in range(len(sortedArray)):
        if sortedArray[i] == target:
            found = True
            return i
        elif sortedArray[i] > target:
            break
    if not found:
        return -1