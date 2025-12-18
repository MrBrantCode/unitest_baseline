"""
QUESTION:
Implement a function `median` that calculates the median of the elements in a given list `l` using a comparison function `cmp_func` without sorting or using built-in functions. The function should handle lists with an even or odd number of elements, manage duplicates, and raise an exception for empty lists or lists with mixed data types.
"""

def median(l, cmp_func):
    if not l:
        raise Exception('ERROR: Empty List')
    try:
        if len(l) % 2 == 1:
            def partition(l, low, high, pivot_index, cmp_func):
                pivot_value = l[pivot_index]
                l[high], l[pivot_index] = l[pivot_index], l[high]
                store_index = low
                for i in range(low, high):
                    if cmp_func(l[i], pivot_value):
                        l[store_index], l[i] = l[i], l[store_index]
                        store_index += 1
                l[high], l[store_index] = l[store_index], l[high]
                return store_index

            def quickSelect(l, low, high, k, cmp_func):
                if low == high:
                    return l[low]
                pivot_index = low + ((high - low) >> 1)
                pivot_index = partition(l, low, high, pivot_index, cmp_func)
                if k == pivot_index:
                    return l[k]
                elif k < pivot_index:
                    return quickSelect(l, low, pivot_index-1, k, cmp_func)
                else:
                    return quickSelect(l, pivot_index+1, high, k, cmp_func)

            return quickSelect(l, 0, len(l) - 1, len(l) // 2, cmp_func)
        else:
            def partition(l, low, high, pivot_index, cmp_func):
                pivot_value = l[pivot_index]
                l[high], l[pivot_index] = l[pivot_index], l[high]
                store_index = low
                for i in range(low, high):
                    if cmp_func(l[i], pivot_value):
                        l[store_index], l[i] = l[i], l[store_index]
                        store_index += 1
                l[high], l[store_index] = l[store_index], l[high]
                return store_index

            def quickSelect(l, low, high, k, cmp_func):
                if low == high:
                    return l[low]
                pivot_index = low + ((high - low) >> 1)
                pivot_index = partition(l, low, high, pivot_index, cmp_func)
                if k == pivot_index:
                    return l[k]
                elif k < pivot_index:
                    return quickSelect(l, low, pivot_index-1, k, cmp_func)
                else:
                    return quickSelect(l, pivot_index+1, high, k, cmp_func)

            return 0.5 * (quickSelect(l, 0, len(l) - 1, len(l) // 2 - 1, cmp_func) + quickSelect(l, 0, len(l) - 1, len(l) // 2, cmp_func))
    except Exception:
        raise Exception('ERROR: Mixed data types')