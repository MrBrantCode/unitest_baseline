"""
QUESTION:
Implement a function `median(lst)` that takes a list of numbers as input and returns the median of the elements in the list without sorting it or using built-in functions. The function should handle duplicate elements, tuples comprising both even and odd number of components, and accurately calculate the median for lists with large numbers.
"""

def quickselect_median(lst):
    def partition(l, low, high):
        pivot = l[high]
        i = low - 1
        for j in range(low, high):
            if l[j] <= pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
        l[i+1], l[high] = l[high], l[i+1]
        return i + 1

    def quickselect(l, k, low, high):
        if low == high: 
            return l[low]
        pi = partition(l, low, high)
        if k == pi:
            return l[k]
        elif k < pi:
            return quickselect(l, k, low, pi-1)
        else:
            return quickselect(l, k, pi+1, high)

    n = len(lst)
    if n % 2 == 1:
        return quickselect(lst, n // 2, 0, n - 1)
    else:
        return 0.5 * (quickselect(lst, n // 2 - 1, 0, n - 1) + quickselect(lst, n // 2, 0, n - 1))