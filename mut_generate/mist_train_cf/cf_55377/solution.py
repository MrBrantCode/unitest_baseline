"""
QUESTION:
Write a recursive function `find_min` that takes a list of elements as input and returns the smallest integer value present in the list. If the list is empty or contains no integers, return the message "empty list or no integers". The list may contain non-integer elements, and the function should ignore them when finding the minimum.
"""

def find_min(num_list, min_num=None):
    if not num_list:
        if min_num is None:
            return "empty list or no integers"
        else:
            return min_num
    else:
        n = num_list.pop()
        if isinstance(n, int):
            if min_num is None or n < min_num:
                min_num = n
        return find_min(num_list, min_num)