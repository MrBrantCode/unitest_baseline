"""
QUESTION:
Write a function `max_sum(lst)` that finds the maximum possible sum of a contiguous subsequence in a given list of integers, excluding any subsequence containing both positive and negative integers. The function should take a list of integers as input and return the maximum possible sum. The function must have a time complexity of O(n), where n is the length of the input list.
"""

def max_sum(lst):
    """
    Finds the maximum possible sum of a contiguous subsequence in a given list of integers,
    excluding any subsequence containing both positive and negative integers.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The maximum possible sum.
    """
    def max_subarray_sum(sublist):
        max_sum = sublist[0]
        curr_sum = sublist[0]
        for num in sublist[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum

    pos_lst = [num for num in lst if num >= 0]
    neg_lst = [num for num in lst if num < 0]

    if not pos_lst:
        return sum(neg_lst)
    elif not neg_lst:
        return sum(pos_lst)
    else:
        return max(max_subarray_sum(pos_lst), max_subarray_sum(neg_lst))