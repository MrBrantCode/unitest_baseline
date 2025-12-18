"""
QUESTION:
You are given an integer array `nums` of length `n`. Define the rotation function `F` on `nums` as `F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]`, where `arrk` is an array obtained by rotating `nums` by `k` positions clock-wise. Implement a function `maxRotateFunction(nums)` that returns a tuple containing the maximum value of `F(0), F(1), ..., F(n-1)` and the corresponding `k` value.
"""

def maxRotateFunction(nums):
    """
    This function calculates the maximum value of F(0), F(1), ..., F(n-1) and the corresponding k value.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the maximum value of F(0), F(1), ..., F(n-1) and the corresponding k value.
    """
    n = len(nums)
    F = sum(i * num for i, num in enumerate(nums))
    total = sum(nums)
    max_F = F
    max_k = 0

    for k in range(n - 1, 0, -1):
        F += total - n * nums[k]
        if F > max_F:
            max_F = F
            max_k = n - k

    return (max_F, max_k)