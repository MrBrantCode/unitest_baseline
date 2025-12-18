"""
QUESTION:
Implement a function called `bubble_sort` that sorts a list of numbers in ascending order without using built-in sorting functions or methods. The function should have a time complexity of O(n^2) and return the sorted list.
"""

def entance(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n-1):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr