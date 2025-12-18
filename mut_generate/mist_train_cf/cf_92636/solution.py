"""
QUESTION:
Design a function `max_subarray(arr, k)` that finds the maximum subarray of an array `arr` containing at least `k` elements. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the array. If no valid subarray with at least k elements exists, the function should return an empty subarray.
"""

def max_subarray(arr, k):
    max_sum = float('-inf')
    current_sum = 0
    start_index = 0
    end_index = 0
    curr_len = 0
    max_len = 0
    
    for i in range(len(arr)):
        num = arr[i]
        current_sum += num
        curr_len += 1
        
        if current_sum > max_sum:
            max_sum = current_sum
            end_index = i
            max_len = curr_len
        
        if current_sum < 0:
            current_sum = 0
            start_index = i + 1
            curr_len = 0
    
    if max_len < k:
        return []
    
    return arr[start_index:end_index+1]