"""
QUESTION:
Implement the function `findMaxAverage(nums, k)` that takes an array of integers `nums` and an integer `k` as input, and returns the maximum average value of a contiguous subarray of `nums` with a length of at least `k`. The function should return a floating-point number with a precision of at least `10^-5`. The length of `nums` is denoted by `n`, where `1 ≤ k ≤ n ≤ 10^4`, and each element in `nums` is within the range `[-10^4, 10^4]`.
"""

def findMaxAverage(nums, k):
    """
    This function calculates the maximum average value of a contiguous subarray of 'nums' with a length of at least 'k'.

    Args:
    - nums (list): An array of integers.
    - k (int): The minimum length of the subarray.

    Returns:
    - float: The maximum average value of a contiguous subarray of 'nums' with a length of at least 'k'.
    """

    eps = 1e-5
    min_num = min(nums)
    max_num = max(nums)

    def canFind(num):
        """
        Helper function to check if a subarray with an average more than 'num' exists.

        Args:
        - num (float): The potential average value.

        Returns:
        - bool: True if a subarray with an average more than 'num' exists, False otherwise.
        """
        sums = [0]
        for i in range(1, len(nums) + 1):
            sums.append(sums[-1] + nums[i - 1] - num)
        min_sum = 0
        for i in range(k, len(nums) + 1):
            if sums[i] >= min_sum:
                return True
            min_sum = min(min_sum, sums[i - k + 1])
        return False

    while max_num - min_num > eps:
        mid_num = min_num + (max_num - min_num) / 2
        if canFind(mid_num):
            min_num = mid_num
        else:
            max_num = mid_num
    return min_num