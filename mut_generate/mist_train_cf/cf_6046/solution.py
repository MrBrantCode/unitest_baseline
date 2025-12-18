"""
QUESTION:
Write a function `highest_sum_divisible_by_four` that takes an array of integers as input and returns the highest sum that can be obtained by including at most three different members from the array, such that no two members have the same index and the sum is divisible by 4. The function should have a time complexity of O(n log n), where n is the size of the array.
"""

def highest_sum_divisible_by_four(arr):
    """
    Returns the highest sum that can be obtained by including at most three different members 
    from the array, such that no two members have the same index and the sum is divisible by 4.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The highest sum that meets the conditions.
    """
    arr.sort()
    maxSum1 = maxSum2 = maxSum3 = float('-inf')
    for num in arr:
        sum1 = num
        sum2 = maxSum1 + num
        sum3 = maxSum2 + num
        if sum1 % 4 == 0 and sum1 > maxSum1:
            maxSum1 = sum1
        if sum2 % 4 == 0 and sum2 > maxSum2:
            maxSum2 = sum2
        if sum3 % 4 == 0 and sum3 > maxSum3:
            maxSum3 = sum3
    return max(maxSum1, maxSum2, maxSum3)