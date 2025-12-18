"""
QUESTION:
Implement the function `sort(array)` that takes a list of integers as input and returns the sorted list in ascending order. The function should use an efficient algorithm and handle lists of any length. The input list will contain at least one element.
"""

def sort(array): 
    length = len(array) 
  
    for i in range(length): 
  
        j = i 
        while j > 0 and array[j-1] > array[j]: 
            # Swap elements
            array[j], array[j-1] = array[j-1], array[j] 
            j -= 1

    return array