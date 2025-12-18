"""
QUESTION:
Implement the function `median(l: list, cmp_func: callable)` which returns the median of elements in a list without sorting it or using built-in functions. The function should handle lists with varying amounts of elements and duplicates, and apply a custom comparison function. The comparison function `cmp_func` takes two parameters and returns a boolean value indicating whether the first element is smaller than the second.
"""

def entance(l, cmp_func):
    def partition(lst, begin, end):
        pivot_idx = begin
        for i in range(begin+1, end+1):
            if cmp_func(lst[i], lst[begin]):
                pivot_idx += 1
                lst[i], lst[pivot_idx] = lst[pivot_idx], lst[i]
        lst[pivot_idx], lst[begin] = lst[begin], lst[pivot_idx]
        return pivot_idx

    def quickselect(lst, begin, end, k):
        if begin == end:
            return lst[begin]

        pivot_idx = partition(lst, begin, end)
        if k == pivot_idx:
            return lst[k]
        elif k < pivot_idx:
            return quickselect(lst, begin, pivot_idx-1, k)
        else:
            return quickselect(lst, pivot_idx+1, end, k)

    if len(l) % 2 == 1:
        return quickselect(l, 0, len(l)-1, len(l)//2)
    else:
        return 0.5 * (quickselect(l, 0, len(l)-1, len(l)//2 - 1) +
                      quickselect(l, 0, len(l)-1, len(l)//2))