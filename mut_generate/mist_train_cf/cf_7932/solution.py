"""
QUESTION:
Write a function `find_kth_smallest` that takes a list of integers `nums` and an integer `k` as input and returns the kth smallest element in the list. The function should not use any built-in functions or libraries that directly calculate the kth smallest element. The algorithm should have a time complexity of O(nlogk) and a space complexity of O(k).
"""

import random

def findKthSmallest(nums, k):
    def partition(nums, left, right):
        pivot = nums[right]  
        i = left - 1  

        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    def quick_select(nums, left, right, k):
        if left == right:
            return nums[left]

        pivot_index = partition(nums, left, right)

        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index > k:
            return quick_select(nums, left, pivot_index - 1, k)
        else:
            return quick_select(nums, pivot_index + 1, right, k)

    return quick_select(nums, 0, len(nums) - 1, k - 1)