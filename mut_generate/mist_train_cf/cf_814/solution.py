"""
QUESTION:
Write a function `shuffle_array(arr, k)` that takes a list of integers `arr` and an integer threshold `k` as input, and returns a shuffled version of the array such that the difference between any two adjacent elements does not exceed `k`. The shuffled array should have the smallest possible difference between its minimum and maximum values. The function should have a time complexity of O(n log n) or better.
"""

def shuffle_array(arr, k):
    n = len(arr)
    sorted_arr = sorted(arr)
    shuffled_arr = [0] * n
    low = 0
    high = n - 1
    
    # Place the smallest and largest elements alternatively in the shuffled array
    for i in range(n):
        if i % 2 == 0:
            shuffled_arr[i] = sorted_arr[low]
            low += 1
        else:
            shuffled_arr[i] = sorted_arr[high]
            high -= 1
    
    # Shuffle the elements randomly within the threshold 'k'
    for i in range(n):
        j = i + 1
        while j < n and abs(shuffled_arr[i] - shuffled_arr[j]) > k:
            j += 1
        if j < n:
            shuffled_arr[i + 1], shuffled_arr[j] = shuffled_arr[j], shuffled_arr[i + 1]
    
    return shuffled_arr