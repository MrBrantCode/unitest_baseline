"""
QUESTION:
Write a function `delete_element(array, index)` that deletes an element at a given index from an array while maintaining the order of the remaining elements. The function should have a time complexity of O(n), where n is the length of the array, and use only constant space without creating any additional data structures. The function should return the modified array.
"""

def delete_element(array, index):
    n = len(array)
    currentIndex = index

    while currentIndex < n-1:
        array[currentIndex] = array[currentIndex+1]
        currentIndex += 1
    
    array[n-1] = 0

    return array