"""
QUESTION:
Write a function `third_largest_unique` that takes a multidimensional array as input and returns the third largest unique number in the array. The function should handle negative numbers and return `None` if the array has less than three unique numbers. The function should not use any built-in sorting functions.
"""

def third_largest_unique(array, unique_nums=None):
    if unique_nums is None:
        unique_nums = set()

    for v in array:
        if isinstance(v, list):
            third_largest_unique(v, unique_nums)
        else:
            unique_nums.add(v)

    unique_nums_list = list(unique_nums)

    if len(unique_nums_list) < 3:
        return None

    top1 = top2 = top3 = float('-inf')
    for num in unique_nums_list:
        if num > top1:
            top1, top2, top3 = num, top1, top2
        elif num > top2:
            top2, top3 = num, top2
        elif num > top3:
            top3 = num

    return top3