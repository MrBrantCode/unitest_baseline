"""
QUESTION:
Implement a function named `find_pair(array)` that takes an array of integers as input and returns the indices of a pair of integers in the array whose sum is divisible by 10. If multiple pairs exist, return the indices of the pair with the maximum absolute difference between the indices. If no such pair exists, return an empty array. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def find_pair(array):
    left = 0
    right = len(array) - 1
    
    max_diff = -1
    max_indices = []
    
    while left < right:
        pair_sum = array[left] + array[right]
        if pair_sum % 10 == 0:
            return [left, right]
        
        if pair_sum < 10:
            left += 1
        else:
            right -= 1
            
        if abs(left - right) > max_diff:
            max_diff = abs(left - right)
            max_indices = [left, right]
    
    return max_indices