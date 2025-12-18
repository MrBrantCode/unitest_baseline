"""
QUESTION:
Write a function called `find_kth_smallest` that takes an array of integers and an integer k as input, and returns the kth smallest element in the array. The function must have a time complexity of O(n) and must use a constant amount of extra space. The function cannot use any sorting algorithms or built-in functions.
"""

def find_kth_smallest(arr, k):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
    
    low = 0
    high = len(arr) - 1
    
    while True:
        pivot_index = partition(arr, low, high)
        
        if pivot_index == k - 1:
            return arr[pivot_index]
        elif pivot_index > k - 1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1