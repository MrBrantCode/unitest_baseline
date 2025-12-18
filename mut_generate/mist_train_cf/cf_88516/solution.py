"""
QUESTION:
Implement the `bubble_sort` function, which takes a list of integers as input and returns the sorted list in ascending order. The function must use the bubble sort algorithm, have a time complexity of O(n^2), and not use any built-in sorting functions, libraries, or additional data structures beyond the input list. The function should modify the input list in-place.
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