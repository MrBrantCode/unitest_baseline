"""
QUESTION:
Implement a function `insertElement(array, element, index)` that inserts an element at a specific index in a dynamically sized array without using built-in functions. The function should handle both out-of-bounds and invalid input scenarios gracefully.
"""

def insertElement(array, element, index):
    # If index is out of bounds
    if index < 0 or index > len(array):
        return "Index out of range"
    else:
        # Create a new array of size one more than the original array
        newArray = [None] * (len(array) + 1)

        # Copy elements from old array to new array upto the index
        for i in range(index):
            newArray[i] = array[i]
        
        # Add new element at given index
        newArray[index] = element

        # Copy the remaining elements from old array to new array
        for i in range(index, len(array)):
            newArray[i+1] = array[i]

        return newArray