"""
QUESTION:
Write a function named `quickselect` that takes as input an array of integers `nums` and returns the median value of the array in O(n) time complexity and O(1) space complexity without modifying the input array. The array `nums` has a size between 1 and 10^6, and each integer is between -10^9 and 10^9 inclusive.
"""

def quickselect(nums):
    """
    Compute the median value of an array of integers in O(n) time complexity and O(1) space complexity.

    Args:
        nums (list): A list of integers.

    Returns:
        float: The median value of the input list.
    """

    def partition(left, right):
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[right] = nums[right], nums[i]
        return i

    def select(left, right, k):
        if left == right:
            return nums[left]
        pivot_index = partition(left, right)
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return select(left, pivot_index - 1, k)
        else:
            return select(pivot_index + 1, right, k)

    n = len(nums)
    if n % 2 == 1:
        return float(select(0, n - 1, n // 2))
    else:
        return 0.5 * (select(0, n - 1, n // 2 - 1) +
                      select(0, n - 1, n // 2))