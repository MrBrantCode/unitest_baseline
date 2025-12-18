"""
QUESTION:
Write a function named 'count_unique_pairs' that takes a list of numbers and a target sum as input, and returns the count of unique pairs along with the pairs themselves whose sum is equal to the given target sum. The function should handle negative numbers and zeros in the list, and it should not consider repeated pairs (i.e., if the pair (a, b) is counted, then (b, a) should not be counted as a separate pair). The function should not use any built-in Python functions or libraries. The output should be a tuple containing the count of unique pairs and a list of tuples, where each tuple contains two elements that add up to the given target sum. The order of the pairs and the order of elements within each pair does not matter.
"""

def entance(nums, target):
    pairs = []
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if (nums[i] + nums[j]) == target:
                pair = sorted([nums[i], nums[j]])
                if pair not in pairs:
                    pairs.append(pair)
    
    count = len(pairs)
    pairs = [tuple(p) for p in pairs]
    return count, pairs