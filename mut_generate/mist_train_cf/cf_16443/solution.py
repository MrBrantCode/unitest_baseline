"""
QUESTION:
Write a function `median(arr)` that computes the median value of all elements in an array of size n (1 <= n <= 10^6) of integers, where each integer is between -10^9 and 10^9 inclusive. The function should compute the median value in O(n) time complexity and O(1) space complexity.
"""

def median(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        
        return i + 1
    
    def quick_select(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if pivot_index == k:
            return arr[pivot_index]
        
        if pivot_index < k:
            return quick_select(arr, pivot_index+1, high, k)
        
        return quick_select(arr, low, pivot_index-1, k)
    
    n = len(arr)
    if n % 2 == 0:
        median_index = n // 2 - 1
        return (quick_select(arr, 0, n-1, median_index) + quick_select(arr, 0, n-1, median_index+1)) / 2
    else:
        median_index = n // 2
        return quick_select(arr, 0, n-1, median_index)