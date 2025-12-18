"""
QUESTION:
Write a function called `bubble_sort` that sorts an array of integers in ascending order using the bubble sort algorithm. The function should iterate through the array as few times as possible, and it should be able to handle arrays that contain duplicate numbers. The function should return the sorted array. The input array can be of any length and may contain any integer values.
"""

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        # Flag to check if any swaps occurred in this iteration
        swapped = False
        
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                # Swap the elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        
        # If no swaps occurred in this iteration, the array is already sorted
        if not swapped:
            break
    
    return nums