"""
QUESTION:
Design a function named `partition_array` that takes an array of integers as input and partitions it into two subarrays such that the difference between the sum of the two subarrays is minimum. The function should return the two subarrays. The function must have a time complexity of O(n^2 * 2^n), where n is the size of the input array.
"""

def partition_array(array):
    n = len(array)
    
    min_diff = float('inf')
    partition1 = []
    partition2 = []
    
    for i in range(1, 2**n):
        subset1 = [array[j] for j in range(n) if (i >> j) & 1]
        subset2 = [array[j] for j in range(n) if not (i >> j) & 1]
        diff = abs(sum(subset1) - sum(subset2))
        
        if diff < min_diff:
            min_diff = diff
            partition1 = subset1
            partition2 = subset2
    
    return partition1, partition2