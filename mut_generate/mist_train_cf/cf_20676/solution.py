"""
QUESTION:
Design a function `maxSubarray(array, k)` that takes an array of integers and an integer `k` as input and returns the maximum subarray of length `k` or more. The function should have a time complexity of O(n log n) and a space complexity of O(log n).
"""

def maxSubarray(array, k):
    def findMaxCrossingSubarray(low, mid, high):
        left_sum = float('-inf')
        max_left_index = mid
        sum = 0
        for i in range(mid, low - 1, -1):
            sum += array[i]
            if sum > left_sum:
                left_sum = sum
                max_left_index = i
        
        right_sum = float('-inf')
        max_right_index = mid + 1
        sum = 0
        for i in range(mid + 1, high + 1):
            sum += array[i]
            if sum > right_sum:
                right_sum = sum
                max_right_index = i
        
        return max_left_index, max_right_index, left_sum + right_sum

    def maxSubarrayHelper(low, high, k):
        if low == high:
            return low, high, array[low]
        
        mid = (low + high) // 2
        
        max_left = maxSubarrayHelper(low, mid, k)
        max_right = maxSubarrayHelper(mid + 1, high, k)
        max_crossing = findMaxCrossingSubarray(low, mid, high)
        
        if max_left[2] >= max_right[2] and max_left[2] >= max_crossing[2]:
            return max_left
        elif max_right[2] >= max_left[2] and max_right[2] >= max_crossing[2]:
            return max_right
        else:
            return max_crossing
    
    return maxSubarrayHelper(0, len(array) - 1, k)