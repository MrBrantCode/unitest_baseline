"""
QUESTION:
Create a function called `can_arrange` that takes an array of unique integers as input and returns a dictionary containing three values: 
- The largest index of an element that is not greater than or equal to the element immediately preceding it.
- The index of the next smallest element that can be swapped to potentially correct the order.
- The minimum number of necessary swaps to correctly sort the array. 

If no unsorted element exists, return {'index': -1, 'swap_with': -1, 'num_swaps': 0}.
"""

def can_arrange(arr):
    index = -1
    swap_with = -1
    num_swaps = 0
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            index = i
            break
            
    if index != -1:
        for j in range(len(arr)):
            if arr[j] > arr[index]:
                swap_with = j
                break
      
        num_swaps = index - swap_with
        
    return {'index': index, 'swap_with': swap_with, 'num_swaps': num_swaps}