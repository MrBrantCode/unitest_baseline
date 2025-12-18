"""
QUESTION:
Create a function named `bubble_sort` that sorts a given list of unique integers in ascending order. The list will have a length between 2 and 10^4 (inclusive). The solution must have a time complexity of O(n^2) and a space complexity of O(1).
"""

def entance(nums):
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