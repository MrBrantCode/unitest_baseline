"""
QUESTION:
Write a function `find_kth_smallest(lst, k)` that finds the kth smallest element in a list `lst`. The list can contain duplicates, negative numbers, and non-integer elements. The function should be optimized for time complexity and should not use any built-in sorting functions. If the list contains non-integer elements, they should be treated as numbers for the purpose of comparison. The function should return the kth smallest element in the list.
"""

def find_kth_smallest(lst, k):
    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i+1], lst[high] = lst[high], lst[i+1]
        return i+1

    def quickselect(lst, low, high, k):
        if low == high:
            return lst[low]
        pivot_index = partition(lst, low, high)
        if k == pivot_index:
            return lst[pivot_index]
        elif k < pivot_index:
            return quickselect(lst, low, pivot_index-1, k)
        else:
            return quickselect(lst, pivot_index+1, high, k)

    # Convert non-integer elements to float
    lst = [float(x) if not isinstance(x, (int, float)) else x for x in lst]

    return quickselect(lst, 0, len(lst)-1, k-1)