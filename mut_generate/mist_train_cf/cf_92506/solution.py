"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of numbers as input and returns the sorted list without using Python's built-in sort function or any other built-in functions or libraries. The function should implement a sorting algorithm.
"""

def entance(nums):
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