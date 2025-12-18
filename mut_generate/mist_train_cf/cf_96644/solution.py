"""
QUESTION:
Write a class `SmallestElement` with methods `find_using_linear_search` and `find_using_selection_sort` that find the smallest element in a given list of integers. The class should also have an `is_sorted` method to check if the list is sorted in non-decreasing order. The methods should handle empty lists, lists with duplicate smallest elements, and lists with negative numbers. The `find_using_linear_search` method should have a time complexity of O(n), and the `find_using_selection_sort` method should have a time complexity of O(n^2).
"""

def entance(nums):
    if len(nums) == 0:
        return "Error: Empty list"
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num
    return smallest