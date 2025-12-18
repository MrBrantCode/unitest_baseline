"""
QUESTION:
Create a function named `get_positive_and_sort` that takes a list of integers as input, filters out non-positive integers, and returns the remaining integers sorted in ascending order. The function should also include a helper function named `swap_elements` to swap two elements in the list.
"""

def get_positive_and_sort(lst):
    """Return only positive numbers in the list, sorted in ascending order."""
    
    def swap_elements(nums, index1, index2):
        # Implement a helper function for sorting elements
        nums[index1], nums[index2] = nums[index2], nums[index1]
    
    positive_nums = [num for num in lst if num > 0]
    
    # Bubble sort algorithm
    for i in range(len(positive_nums)):
        for j in range(len(positive_nums) - 1):
            if positive_nums[j] > positive_nums[j + 1]:
                swap_elements(positive_nums, j, j + 1)
    
    return positive_nums