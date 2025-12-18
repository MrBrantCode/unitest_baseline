"""
QUESTION:
Implement a function named `quick_sort` that sorts a list of distinct integers using the Quick Sort algorithm. The function should have a time complexity of O(n log n) and a space complexity of O(log n), where n is the length of the input list. The function should not use any built-in sorting functions and should be able to handle lists containing up to 10^6 elements with any integer values (positive or negative) or empty lists.
"""

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        smaller = [x for x in nums[1:] if x <= pivot]
        greater = [x for x in nums[1:] if x > pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(greater)