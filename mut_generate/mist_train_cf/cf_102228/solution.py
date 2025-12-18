"""
QUESTION:
Implement a function `insertElement` that inserts a new element at the beginning of an unsorted array of integers without using any built-in array functions or methods. The function should have a time complexity of O(n) and space complexity of O(n), where n is the number of elements in the array. The function should take two arguments: the array and the new element to be inserted, and return the new array with the element inserted at the beginning.
"""

def insertElement(array, newElement):
    newArray = [None] * (len(array) + 1)
    newArray[0] = newElement
    for i in range(len(array)):
        newArray[i+1] = array[i]
    return newArray