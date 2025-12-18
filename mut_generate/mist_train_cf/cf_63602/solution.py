"""
QUESTION:
Create a function `max_len_subarray(lst)` that finds the maximum length of a strictly monotonic subarray in a given list `lst`. The function should return a tuple containing the maximum length and the starting and ending indices of the maximum length subarray. The function should handle lists with less than 2 elements. The list `lst` will only contain integers.
"""

def max_len_subarray(lst):
    n = len(lst)
    
    if n < 2: 
        if n == 0: return 0, None, None
        return 1, 0, 0

    max_len = 1
    cur_len = 1
    start = 0
    max_start = 0
    max_end = 0
    direction = None

    for i in range(1, n):
        if (lst[i-1] < lst[i] and (cur_len == 1 or direction == 'increasing')) or \
           (lst[i-1] > lst[i] and (cur_len == 1 or direction == 'decreasing')):
            cur_len += 1
            if lst[i-1] < lst[i]: direction = 'increasing'
            if lst[i-1] > lst[i]: direction = 'decreasing'
            if cur_len > max_len:
                max_len = cur_len
                max_start = start
                max_end = i
        else:
            cur_len = 2
            start = i-1
            if lst[i-1] < lst[i]: direction = 'increasing'
            if lst[i-1] > lst[i]: direction = 'decreasing'
            
    return max_len, max_start, max_end