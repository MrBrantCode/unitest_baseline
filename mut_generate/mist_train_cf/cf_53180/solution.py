"""
QUESTION:
Write a function named `max_sum` that takes an array and a window size as inputs. The function should return the maximum accumulative sum corresponding to a continuous fraction of the stipulated magnitude 'k' within the array. The array size must be greater than the window size 'k'.
"""

def max_sum(arr, k):
    array_size = len(arr)
    # n must be greater than k
    if array_size <= k:
        return -1
    # Compute sum of first window of size k
    window_sum = sum([arr[i] for i in range(k)])
    max_sum = window_sum
    # Compute sums of remaining windows by removing elements from start
    # and adding elements from end
    for i in range(array_size - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
 
    return max_sum