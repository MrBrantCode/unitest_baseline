"""
QUESTION:
Write a function `find_pairs` that takes a list `nums` containing integer and string values, and an integer `k` as input. The function should return a list of tuples, where each tuple contains a pair of identical elements (regardless of data type) and their respective positions `i` and `j` in the list, such that the absolute difference between `i` and `j` does not exceed `k`. The comparison should not be type strict, meaning that `1` and `'1'` should be considered identical.
"""

def find_pairs(nums, k):
    indices = {} 
    results = []

    for index, num in enumerate(nums):
        num = str(num) 

        if num in indices and index - indices[num] <= k:
            results.append((num, indices[num], index)) 

        indices[num] = index 

    return results