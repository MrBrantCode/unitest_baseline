"""
QUESTION:
Implement the `partition`, `quickSelect`, and `median` functions. 

- `partition(l, low, high, pivot_index, cmp_func)`: Rearrange the list `l` such that elements less than the pivot are on the left of it, and elements greater are on the right. The `cmp_func` is a comparison function used to determine the order of elements. 
- `quickSelect(l, low, high, k, cmp_func)`: Find the k-th smallest element in the list `l` using the quickselect algorithm. The `cmp_func` is a comparison function used to determine the order of elements. 
- `median(l, cmp_func)`: Find the median of the list `l`. If the list has an even number of elements, the median is the average of the two middle elements. The `cmp_func` is a comparison function used to determine the order of elements. 

Note: `cmp_func` should be a function that takes two arguments and returns `True` if the first argument is less than the second, and `False` otherwise.
"""

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

def median(l, cmp_func):
    if not l:
        raise Exception('ERROR: Empty List')
    try:
        if len(l) % 2 == 1:
            return quickSelect(l, 0, len(l) - 1, len(l) // 2, cmp_func)
        else:
            return 0.5 * (quickSelect(l, 0, len(l)-1, len(l)//2 - 1, cmp_func) + quickSelect(l, 0, len(l) - 1, len(l)//2, cmp_func))
    except Exception:
        raise Exception('ERROR: Mixed data types')