"""
QUESTION:
Create a function called `sort_list` that takes a list of integers as input, removes any duplicate numbers from the list, and sorts the remaining numbers in ascending order. The function must not use any built-in sorting functions or libraries to sort the list.
"""

def sort_list(nums):
    # Remove duplicates from the list
    nums = list(set(nums))

    # Bubble sort algorithm to sort the list
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums