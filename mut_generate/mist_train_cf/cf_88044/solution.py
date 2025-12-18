"""
QUESTION:
Implement the `selection_sort` function to sort an array in descending order without using any built-in sorting functions or methods. The function should have a time complexity of O(n^2) and a space complexity of O(1). The input is a list of integers and the output should be the sorted list.
"""

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the maximum element in the remaining unsorted array
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        
        # Swap the found maximum element with the first element
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    return arr