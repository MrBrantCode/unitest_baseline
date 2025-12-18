"""
QUESTION:
Write a function `insertElement` that takes a sorted array and a new element as input and returns a new sorted array with the new element inserted, without using any built-in sorting functions or libraries. The new element should be inserted at the correct position in the sorted array. The function should handle the case where the new element is larger or smaller than all existing elements in the array. The function should return the new sorted array.
"""

def insertElement(sortedArray, element):
    index = 0
    for i in range(len(sortedArray)):
        if sortedArray[i] > element:
            break
        index += 1

    newArray = [0] * (len(sortedArray) + 1)
    
    for i in range(index):
        newArray[i] = sortedArray[i]
    
    newArray[index] = element
    
    for i in range(index, len(sortedArray)):
        newArray[i + 1] = sortedArray[i]
    
    return newArray