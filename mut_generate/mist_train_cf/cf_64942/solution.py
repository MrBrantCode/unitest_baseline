"""
QUESTION:
Implement a function named `cocktail_sort` that sorts a list of decimal numbers in ascending or descending order. The function should take two parameters: a list of decimal numbers and an optional boolean argument `ascending` that defaults to `True` for ascending sort and `False` for descending sort.
"""

def cocktail_sort(nums, ascending=True):
    swapped = True
    start = 0
    end = len(nums) - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if (nums[i] > nums[i + 1]) == ascending:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (nums[i] > nums[i + 1]) == ascending:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        start = start + 1
    return nums