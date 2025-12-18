"""
QUESTION:
Implement a function called `count_valid_triplets` that takes an array of integers as input and returns the number of unique triplets that satisfy the triangle inequality, where the sum of any two sides must be greater than the third side. The function should have a time complexity of O(n^2), use constant space complexity, handle negative integers and duplicates correctly, and be implemented without using any built-in sorting functions or libraries.
"""

def count_valid_triplets(nums):
    n = len(nums)
    count = 0

    # Sort the array in non-decreasing order
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    # Fix the first element and use two pointers to find the valid triplets
    for i in range(n - 2):
        k = i + 2
        for j in range(i + 1, n - 1):
            while k < n and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1

    return count