"""
QUESTION:
Create a function `median` that calculates the median of a list `l` containing integers, tuples, and nested lists and tuples. The function should take a custom comparison function `cmp_func` as an argument and use it for comparisons. The function should not use built-in sorting functions or sort the list. If the list has an even number of elements, the median is the average of the two middle elements. The function should be able to handle duplicates and nested elements.
"""

def median(l: list, comparer):
    # flatten the nested list
    def flatten(lst):
        for i in lst:
            if type(i) is list or type(i) is tuple:
                for sub in flatten(i):
                    yield sub
            else:
                yield i

    l = list(flatten(l))

    # find the median
    def select(lst, left, right, median_index):
        while True:
            if left == right:
                return lst[left]
            pivot_index = partition(lst, left, right)
            if median_index == pivot_index:
                return lst[median_index]
            elif median_index < pivot_index:
                right = pivot_index - 1
            else:
                left = pivot_index + 1

    def partition(lst, left, right):
        pivot_value = lst[right]
        i = left - 1
        for j in range(left, right):
            if comparer(pivot_value, lst[j]) > 0:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[right] = lst[right], lst[i + 1]
        return i + 1

    center = len(l) // 2
    if len(l) % 2 == 1:
        return float(select(l, 0, len(l) - 1, center))
    else:
        return (select(l, 0, len(l) - 1, center) + select(l, 0, len(l) - 1, center - 1)) / 2.0