"""
QUESTION:
Write a function named `replace_kth_smallest` that takes two parameters: a list of integers `nums` and an integer `K`. The function replaces the Kth smallest number in the list with the sum of its digits. The function should have a time complexity of O(n log n) and a space complexity of O(1).
"""

def replace_kth_smallest(nums, K):
    # Step 1: Sort the array
    nums.sort()

    # Step 2: Find the Kth smallest number
    kth_smallest = nums[K-1]

    # Step 3: Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(kth_smallest))

    # Step 4: Replace the Kth smallest number with the sum of its digits
    nums[K-1] = digit_sum

    return nums