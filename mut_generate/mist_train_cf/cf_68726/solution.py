"""
QUESTION:
Write a function `find_target_subarrays` that takes a list of integers `my_list` and a target integer `target` as input, and returns the number of contiguous subarrays in `my_list` with a sum equal to `target`. The function should have a time complexity of O(n), where n is the number of elements in `my_list`.
"""

def find_target_subarrays(my_list, target):
    prefix_sum = {0: 1}  
    total = 0
    count = 0
    for num in my_list:
        total += num
        if total - target in prefix_sum:
            count += prefix_sum[total - target]
        if total not in prefix_sum:
            prefix_sum[total] = 0
        prefix_sum[total] += 1
        
    return count