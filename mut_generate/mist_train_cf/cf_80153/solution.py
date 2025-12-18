"""
QUESTION:
Implement a function `quick_sort(nums)` that sorts a list of numerical data using the Quick Sort algorithm. The function should recursively partition the array around a pivot and sort the sub-arrays. The input is a list of integers and the output should be a sorted list of integers. The function should work for lists of any length.
"""

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        less_than_pivot = [x for x in nums[1:] if x <= pivot]
        greater_than_pivot = [x for x in nums[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)