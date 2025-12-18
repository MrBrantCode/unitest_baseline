"""
QUESTION:
Implement a function `bubble_sort` that sorts an array of integers in non-decreasing order using the Bubble Sort algorithm. The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. The input array can have a maximum length of 10^6 and the range of integers in the array is from -10^9 to 10^9. The function should handle cases where the input array is empty or contains duplicate elements.
"""

def bubble_sort(arr):
    n = len(arr)
    
    if n == 0:
        return arr
    
    # Traverse through all array elements
    for i in range(n-1):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr