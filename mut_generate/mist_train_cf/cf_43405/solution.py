"""
QUESTION:
Implement a class with methods `update` and `calculate_sum`. The `update` method takes a list of integers and stores it internally. The `calculate_sum` method takes a start index and an end index as parameters and returns the sum of the integers in the internal list within the specified range (inclusive). The list of integers can have up to 10^5 elements, and the start and end indexes are guaranteed to be within the list limits. The `calculate_sum` method may be called multiple times, so its time complexity should not exceed O(1).
"""

def entrance(nums, start, end):
    prefix_sums = nums[:]
    for i in range(1, len(nums)):
        prefix_sums[i] += prefix_sums[i-1]
        
    if start == 0:
        return prefix_sums[end]
    return prefix_sums[end] - prefix_sums[start-1]