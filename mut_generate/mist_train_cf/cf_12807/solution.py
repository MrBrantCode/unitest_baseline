"""
QUESTION:
Write a function `find_pairs` that takes a list of integers and a target sum as input and returns a list of all pairs of integers from the input list that add up to the target sum. The function should have a time complexity of O(n), where n is the length of the input list.
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