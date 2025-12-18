"""
QUESTION:
Write a function `max_subarray_sum` that finds the maximum sum of all subarrays within a given array of integers. The function should take one parameter, `arr`, which is a list of integers. The function should return the maximum sum found.
"""

def max_subarray_sum(arr):
    """
    Finds the maximum sum of all subarrays within a given array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The maximum sum found.
    """
    def max_crossing_sum(arr, low, mid, high):
        # Find the maximum sum of the subarray that crosses the midpoint
        left_sum = float('-inf')
        sum = 0
        for i in range(mid, low-1, -1):
            sum = sum + arr[i]
            if (sum > left_sum):
                left_sum = sum

        right_sum = float('-inf')
        sum = 0
        for i in range(mid + 1, high + 1):
            sum = sum + arr[i]
            if (sum > right_sum):
                right_sum = sum

        return max(left_sum + right_sum, left_sum, right_sum)

    def max_subarray_sum_util(arr, low, high):
        # Base Case: Only one element
        if (low == high):
            return arr[low]

        # Find the middle point to divide the array into two halves
        mid = (low + high) // 2

        # Return maximum of following three possible cases
        # a) Maximum subarray sum in left half
        # b) Maximum subarray sum in right half
        # c) Maximum subarray sum such that the subarray crosses the midpoint
        return max(max_subarray_sum_util(arr, low, mid),
                   max_subarray_sum_util(arr, mid+1, high),
                   max_crossing_sum(arr, low, mid, high))

    return max_subarray_sum_util(arr, 0, len(arr)-1)