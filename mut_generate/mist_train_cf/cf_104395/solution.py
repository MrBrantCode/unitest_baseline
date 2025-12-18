"""
QUESTION:
Implement a function named `sort_list` that sorts a list of integers in ascending order using the bubble sort algorithm. The function should handle lists containing duplicate elements. The function takes a list of integers as input and returns the sorted list. The function should not modify the original list.
"""

def sort_list(nums):
    sorted_nums = list(nums)  
    n = len(sorted_nums)
    for i in range(n):
        swap = False
        for j in range(0, n-i-1):
            if sorted_nums[j] > sorted_nums[j+1]:
                sorted_nums[j], sorted_nums[j+1] = sorted_nums[j+1], sorted_nums[j]
                swap = True
        if not swap:
            break
    return sorted_nums