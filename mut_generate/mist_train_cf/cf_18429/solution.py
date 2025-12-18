"""
QUESTION:
Write a function `replace_kth_smallest` that takes an integer array `nums` and an integer `K` as input, replaces the Kth smallest number in the array with the sum of its digits, and returns the modified array. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def replace_kth_smallest(nums, K):
    # Sort the array
    nums.sort()

    # Find the Kth smallest number
    kth_smallest = nums[K-1]

    # Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(kth_smallest))

    # Replace the Kth smallest number with the sum of its digits
    nums[K-1] = digit_sum

    return nums