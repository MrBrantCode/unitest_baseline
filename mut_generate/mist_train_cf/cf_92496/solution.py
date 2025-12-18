"""
QUESTION:
Create a function named `find_pairs` that takes two parameters: a list of integers `arr` and a target sum `target_sum`. The function should return a list of all pairs of integers from `arr` that add up to `target_sum`. If there are no such pairs, the function should return an empty list. The function must have a time complexity of O(n), where n is the length of the input list `arr`.
"""

def find_pairs(arr, target_sum):
    pair_list = []
    num_dict = {}
    
    for num in arr:
        complement = target_sum - num
        if complement in num_dict:
            pair_list.append([complement, num])
        num_dict[num] = True
    
    return pair_list