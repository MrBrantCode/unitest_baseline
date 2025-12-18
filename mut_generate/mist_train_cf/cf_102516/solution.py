"""
QUESTION:
Implement the `bubble_sort` function to sort an array of integers in ascending order using the bubble sort algorithm. The function should have a time complexity of O(n^2) and a space complexity of O(1), where n is the length of the array. The function should take an array as input and return the sorted array.
"""

def entance(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr