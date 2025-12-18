"""
QUESTION:
Implement a function `partition(lst, begin, end, cmp_func)` that rearranges the elements of the list `lst` in-place such that all elements less than the pivot element (at index `begin`) are to its left, and all elements greater are to its right, then returns the final index of the pivot element. The comparison function `cmp_func(a, b)` returns `True` if `a` is considered less than `b`. 

Implement another function `quickselect(lst, begin, end, k, cmp_func)` that uses the `partition` function to find the `k-th` smallest element in the list `lst` using the quickselect algorithm and the comparison function `cmp_func`. 

Finally, implement a function `median(l, cmp_func)` that calculates the median of the list `l` using the `quickselect` function and the comparison function `cmp_func`. The median of a list with an even number of elements is the average of the two middle elements.
"""

def partition(lst, begin, end, cmp_func):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if cmp_func(lst[i], lst[begin]):
            pivot_idx += 1
            lst[i], lst[pivot_idx] = lst[pivot_idx], lst[i]
    lst[pivot_idx], lst[begin] = lst[begin], lst[pivot_idx]
    return pivot_idx

def quickselect(lst, begin, end, k, cmp_func):
    if begin == end:
        return lst[begin]

    pivot_idx = partition(lst, begin, end, cmp_func)
    if k == pivot_idx:
        return lst[k]
    elif k < pivot_idx:
        return quickselect(lst, begin, pivot_idx-1, k, cmp_func)
    else:
        return quickselect(lst, pivot_idx+1, end, k, cmp_func)

def median(l, cmp_func):
    if len(l) % 2 == 1:
        return quickselect(l, 0, len(l)-1, len(l)//2, cmp_func)
    else:
        return 0.5 * (quickselect(l, 0, len(l)-1, len(l)//2 - 1, cmp_func) +
                      quickselect(l, 0, len(l)-1, len(l)//2, cmp_func))