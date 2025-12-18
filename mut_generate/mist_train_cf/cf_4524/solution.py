"""
QUESTION:
Implement a function called `bubble_sort` that takes a list of integers as input and returns the sorted list in ascending order using the bubble sort algorithm. The function must have a time complexity of O(n^2), and it must sort the list in-place without using any built-in sorting functions or libraries, additional data structures, or variables besides the given list.
"""

def bubble_sort(nums):
    n = len(nums)
    
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums