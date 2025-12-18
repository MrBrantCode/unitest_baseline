"""
QUESTION:
Implement a function `get_positive_and_sort` that takes a list of integers as input, filters out only the positive numbers, and returns them in ascending order. The function should use a separate helper function, `swap_elements`, to swap two elements in a list. You are not allowed to use the built-in `sort()` or `sorted()` functions. 

Create the `get_positive_and_sort` function to filter the input list, and implement a sorting algorithm using the `swap_elements` helper function to sort the filtered list.
"""

def get_positive_and_sort(nums):
    """Return only positive numbers in the list, sorted in ascending order."""
    
    def swap_elements(n, index1, index2):
        """Swap two elements in a list."""
        temp = n[index1]
        n[index1] = n[index2]
        n[index2] = temp

    positive_nums = [num for num in nums if num > 0]
    
    for i in range(len(positive_nums)):
        for j in range(len(positive_nums) - i - 1):
            if positive_nums[j] > positive_nums[j + 1]:
                swap_elements(positive_nums, j, j + 1)

    return positive_nums