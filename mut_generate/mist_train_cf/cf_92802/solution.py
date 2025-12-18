"""
QUESTION:
Write a function find_longest_subarray(arr, target_sum) that takes in an array of positive integers and a target sum, and returns the longest subarray with a sum equal to the target sum that contains at least one odd and one even integer. If no such subarray exists, return an empty array. The function should return the longest subarray in case of a tie, and should be efficient for large inputs.
"""

def find_longest_subarray(arr, target_sum):
    def has_odd_and_even(subarray):
        has_odd = False
        has_even = False
        
        for num in subarray:
            if num % 2 == 0:
                has_even = True
            else:
                has_odd = True
        
        return has_odd and has_even

    start = 0
    end = 0
    current_sum = 0
    max_sum = 0
    max_start = -1
    max_end = -1
    
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