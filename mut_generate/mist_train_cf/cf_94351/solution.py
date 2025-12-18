"""
QUESTION:
Implement the `quick_sort` function that sorts a list of distinct integers in ascending order using the Quick Sort algorithm with a time complexity of O(n log n) and a space complexity of O(log n). The function should not use any built-in sorting functions and should work for lists of up to 10^6 elements containing any integer values (positive or negative).
"""

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        smaller = [x for x in nums[1:] if x <= pivot]
        greater = [x for x in nums[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)