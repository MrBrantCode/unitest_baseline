"""
QUESTION:
Find the longest subarray in a given array of positive integers that sums up to a target sum and contains at least one odd and one even integer. If no such subarray exists, return an empty array.

The function should take two parameters: an array of positive integers and the target sum. The function should return the longest subarray that meets the conditions. If there are multiple subarrays with the same maximum length, return any of them.
"""

def entrance(arr, target_sum):
    start = 0
    end = 0
    current_sum = 0
    max_sum = 0
    max_start = -1
    max_end = -1

    def has_odd_and_even(arr):
        has_odd = False
        has_even = False
        
        for num in arr:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True
        
        return has_odd and has_even

    while end < len(arr):
        if current_sum < target_sum:
            current_sum += arr[end]
            end += 1
        elif current_sum == target_sum:
            if has_odd_and_even(arr[start:end]):
                if end - start > max_sum:
                    max_sum = end - start
                    max_start = start
                    max_end = end
            current_sum -= arr[start]
            start += 1
        else:
            current_sum -= arr[start]
            start += 1
    
    if max_start == -1:
        return []
    else:
        return arr[max_start:max_end]