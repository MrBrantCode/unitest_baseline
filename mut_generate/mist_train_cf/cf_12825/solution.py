"""
QUESTION:
Implement a function named `bubble_sort` that takes a list of numbers as input, sorts them in ascending order without using Python's built-in sort function or any other built-in functions or libraries, and returns the sorted list.
"""

def bubble_sort(nums):
    n = len(nums)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums