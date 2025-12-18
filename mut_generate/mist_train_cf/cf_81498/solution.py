"""
QUESTION:
Write a function `find_median` that takes an array of distinct integers as input and returns the median value. The function should have a time complexity of O(n). If the array length is even, the median is the average of the two middle numbers; if the array length is odd, the median is the middle number.
"""

def find_median(nums):
    """
    Find the median of an array of distinct integers using QuickSelect.

    Args:
        nums (list): A list of distinct integers.

    Returns:
        float: The median value of the input array.
    """
    n = len(nums)

    def quickselect(k):
        if len(nums) == 1:
            return nums[0]

        pivot_index = len(nums) // 2
        pivot = nums[pivot_index]
        left = [x for i, x in enumerate(nums) if x < pivot and i != pivot_index]
        middle = [x for x in nums if x == pivot]
        right = [x for i, x in enumerate(nums) if x > pivot and i != pivot_index]

        if k <= len(left):
            return quickselect_left(left, k)
        elif k <= len(left) + len(middle):
            return middle[0]
        else:
            return quickselect(right, k - len(left) - len(middle))

    def quickselect_left(left, k):
        if len(left) == 1:
            return left[0]
        pivot_index = len(left) // 2
        pivot = left[pivot_index]
        left_part = [x for i, x in enumerate(left) if x < pivot and i != pivot_index]
        middle = [x for x in left if x == pivot]
        right_part = [x for i, x in enumerate(left) if x > pivot and i != pivot_index]
        if k <= len(left_part):
            return quickselect_left(left_part, k)
        elif k <= len(left_part) + len(middle):
            return middle[0]
        else:
            return quickselect_left(right_part, k - len(left_part) - len(middle))

    if n % 2 == 1:
        return quickselect(n // 2 + 1)
    else:
        return 0.5 * (quickselect(n // 2) + quickselect(n // 2 + 1))