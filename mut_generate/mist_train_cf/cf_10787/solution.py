"""
QUESTION:
Implement the `bubble_sort` function to sort a list of numbers in increasing order without using any built-in sorting functions or libraries. The solution should have a time complexity of O(n^2), where n is the length of the list, and a space complexity of O(1). The input is a list of integers and the output is the sorted list.
"""

def bubble_sort(nums):
    n = len(nums)
    
    # Iterate through the entire list
    for i in range(n):
        
        # Last i elements are already sorted, so no need to compare them again
        for j in range(0, n-i-1):
            
            # Compare adjacent elements and swap if necessary
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    
    return nums