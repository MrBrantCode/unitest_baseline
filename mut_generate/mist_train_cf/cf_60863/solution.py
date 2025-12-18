"""
QUESTION:
Write a function `longest_subarray_with_sum` that finds the longest subarray in a given array that sums up to a target sum. The function should take two parameters: `arr` (the input array) and `target_sum` (the target sum). The function should return a tuple containing the start and end indices of the longest subarray with the given sum.
"""

def longest_subarray_with_sum(arr, target_sum):
    hashmap = dict()
    curr_sum = 0
    max_len = 0
    start_index = 0
    
    for i in range(len(arr)):
        curr_sum += arr[i]

        # check if curr_sum is equal to target sum
        if curr_sum == target_sum:
            max_len = i + 1
            start_index = 0

        # check if current sum minus target sum exists in the hashmap
        if curr_sum - target_sum in hashmap:
            if max_len < i - hashmap[curr_sum - target_sum]:
                max_len = i - hashmap[curr_sum - target_sum]
                start_index = hashmap[curr_sum - target_sum] + 1
        
        # If curr_sum is not present in dictionary then store it
        if curr_sum not in hashmap:
            hashmap[curr_sum] = i

    end_index = start_index + max_len - 1
    subarray = (start_index, end_index)
    return subarray