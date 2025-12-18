"""
QUESTION:
Implement a function named `median` that calculates the median of elements in a given list. This function should handle lists with both even and odd number of elements, and it should correctly handle duplicate elements. The function cannot use sorting methods or existing functions to calculate the median.
"""

def median(l):
    def partition(l, low, high):
        pivot = l[high]
        i = low - 1
        for j in range(low, high):
            if l[j] <= pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
        l[i+1], l[high] = l[high], l[i+1]
        return i + 1

    def quickselect(l, low, high, k):
        if low == high: 
            return l[low]
        pivot_index = partition(l, low, high)
        if k == pivot_index:
            return l[k]
        elif k < pivot_index:
            return quickselect(l, low, pivot_index - 1, k)
        else:
            return quickselect(l, pivot_index + 1, high, k)

    if len(l) % 2 != 0:
        return quickselect(l, 0, len(l) - 1, len(l) // 2)
    else:
        return 0.5 * (quickselect(l, 0, len(l) - 1, len(l) // 2 - 1) +
                      quickselect(l, 0, len(l) - 1, len(l) // 2))