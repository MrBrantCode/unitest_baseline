"""
QUESTION:
Create a function called bubble_sort_duplicates(nums) that takes a list of numbers as input and returns a new list where the numbers are sorted in ascending order and duplicates are grouped together. The function should use the bubble sort algorithm and should not use any built-in sorting functions or libraries. The input list can contain duplicate numbers.
"""

def bubble_sort_duplicates(nums):
    n = len(nums)
    sorted_nums = []
    duplicates = []
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    for j in range(n):
        if j < n-1 and nums[j] == nums[j+1]:
            duplicates.append(nums[j])
        else:
            sorted_nums.append(nums[j])
    
    return sorted_nums + duplicates