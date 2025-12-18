"""
QUESTION:
Create a function `find_median(arr)` that takes an array of integers as input and returns the median value. The function should not modify the input array, have a time complexity of O(nlogn) or less, and a space complexity of O(n) or less. The function should handle arrays with duplicate elements, odd and even number of elements, and minimize the number of comparisons performed. The solution should not use any built-in sorting functions or libraries.
"""

def find_median(arr):
    n = len(arr)
    
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def kth_smallest(arr, low, high, k):
        if low == high:
            return arr[low]
        
        pivot_index = partition(arr, low, high)
        
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return kth_smallest(arr, pivot_index + 1, high, k)
        else:
            return kth_smallest(arr, low, pivot_index - 1, k)
    
    if n % 2 == 0:
        median_index1 = n // 2
        median_index2 = median_index1 - 1
        median = (kth_smallest(arr, 0, n - 1, median_index1) + kth_smallest(arr, 0, n - 1, median_index2)) / 2
    else:
        median_index = n // 2
        median = kth_smallest(arr, 0, n - 1, median_index)
    
    return median