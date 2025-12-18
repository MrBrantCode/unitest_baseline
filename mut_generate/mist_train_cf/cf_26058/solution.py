"""
QUESTION:
Write a function `sortInts` that takes a list of integers as input and returns the sorted list in ascending order. The function should sort the list in-place, meaning it should modify the original list rather than creating a new one.
"""

def sortInts(nums): 
    # Traverse through all array elements 
    for i in range(len(nums)): 
  
        # Last i elements are already in place 
        for j in range(0, len(nums)-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if nums[j] > nums[j+1] : 
                nums[j], nums[j+1] = nums[j+1], nums[j] 
                
    return nums