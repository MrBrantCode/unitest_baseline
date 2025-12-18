"""
QUESTION:
Write a function `canThreePartsEqualSum(arr)` that determines if an array of integers can be partitioned into three non-empty parts with equal sums. The function should return `True` if such a partition is possible and `False` otherwise. The array `arr` has a length between 3 and 5 * 10^4 (inclusive) and each element is an integer between -10^4 and 10^4 (inclusive).
"""

def canThreePartsEqualSum(arr):
    total_sum = sum(arr)
    if total_sum % 3 != 0:
        return False
    
    count, cumulative_sum, target = 0, 0, total_sum // 3
    for num in arr:
        cumulative_sum += num
        if cumulative_sum == target:
            cumulative_sum = 0
            count += 1

    return count >= 3