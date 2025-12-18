"""
QUESTION:
Given a list of integers, write a function `max_sum` that finds the maximum possible sum by selecting a contiguous subsequence from the list, with the restriction that any subsequence containing both positive and negative integers should be excluded. The function should return the maximum possible sum.
"""

def max_sum(lst):
    pos_lst = []
    neg_lst = []
    for num in lst:
        if num >= 0:
            pos_lst.append(num)
        else:
            neg_lst.append(num)
    if not pos_lst:
        return sum(neg_lst)
    elif not neg_lst:
        return sum(pos_lst)
    else:
        max_pos = max_subarray_sum(pos_lst)
        max_neg = max_subarray_sum(neg_lst)
        return max(max_pos, max_neg)

def max_subarray_sum(lst):
    max_sum = lst[0]
    curr_sum = lst[0]
    for num in lst[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum