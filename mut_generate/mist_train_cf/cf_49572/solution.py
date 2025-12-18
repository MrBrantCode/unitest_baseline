"""
QUESTION:
Create a function named `can_arrange` that takes an array of unique integers as input. The function should find the largest index of an element that is not greater than or equal to the element immediately preceding it, and the index of the next smallest element that can be swapped with it to potentially correct the order. If no such element exists, the function should return `{'index': -1, 'swap_with': -1}`.
"""

def can_arrange(arr):
    index = -1
    swap_with = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            index = i
            break
    
    if index != -1:
        for i in range(index-1):
            if arr[i] > arr[index]:
                swap_with = i
                break
                
    return {'index': index, 'swap_with': swap_with}