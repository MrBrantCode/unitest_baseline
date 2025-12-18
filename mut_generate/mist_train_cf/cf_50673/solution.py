"""
QUESTION:
Write a function named `median` that takes a list of numbers as input and returns the median of these numbers. The function should handle lists with both odd and even number of elements, including lists with duplicate elements. The function should not use sorting or built-in functions.
"""

def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    while low <= high:
        while nums[low] < pivot:
            low += 1
        while nums[high] > pivot:
            high -= 1
        if low <= high:
            nums[low], nums[high] = nums[high], nums[low]
            low, high = low + 1, high - 1
    return low 

def select(nums, k):
    low, high = 0, len(nums) - 1
    while high > low:
        pivot = partition(nums, low, high)
        if pivot < k:
            low = pivot
        elif pivot > k:
            high = pivot - 1
        else:
            return nums[k]
    return nums[low]

def median(nums): 
    if len(nums)%2 == 0: 
      return (select(nums, len(nums)//2) + select(nums, len(nums)//2-1))/2 
    else: 
      return select(nums, len(nums)//2)