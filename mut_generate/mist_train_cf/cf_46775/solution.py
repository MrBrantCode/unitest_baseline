"""
QUESTION:
Implement a function called `merged_list` that takes two lists of integers as input. The function should merge the two lists, remove any duplicate elements, and return the resulting list in descending order. The implementation must not use Python's built-in functions for sorting, merging, or removing duplicates.
"""

def merged_list(list1: list, list2: list):
    def quick_sort(nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

    def remove_duplicates(nums):
        result = []
        for num in nums:
            if num not in result:
                result.append(num)
        return result

    nums = list1 + list2
    sorted_nums = quick_sort(nums)
    unique_nums = remove_duplicates(sorted_nums)
    unique_nums.reverse()
    return unique_nums