"""
QUESTION:
Implement the `find_kth_largest` function to find the kth largest number in an array. The function should take two parameters: `arr` (the input array) and `k` (the position of the number to find). The function should have a time complexity of O(n) or better and should not modify the original array or use any built-in sorting functions, data structures, or external libraries. The implementation should be memory efficient and not use additional space proportional to the size of the input array.
"""

def find_kth_largest(arr, k):
    def quick_select(arr, left, right, k):
        if left == right:
            return arr[left]
        
        pivot_index = partition(arr, left, right)
        
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            return quick_select(arr, pivot_index + 1, right, k)
        else:
            return quick_select(arr, left, pivot_index - 1, k)

    def partition(arr, left, right):
        pivot = arr[right]
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        
        return i + 1

    if k < 1 or k > len(arr):
        return None
    
    return quick_select(arr, 0, len(arr) - 1, len(arr) - k)