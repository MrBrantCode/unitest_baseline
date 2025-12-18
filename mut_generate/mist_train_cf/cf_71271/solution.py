"""
QUESTION:
Create a function `advanced_median` that takes a list `l` and a comparison function `cmp_func` as input. The function should calculate the median of the elements in the list without sorting it. It should be able to handle lists with mixed data types (integer, float, string), tuples with variable sizes, and duplicates. If the comparison function cannot compare two elements or if an error occurs during the calculation, the function should print an error message and return `None`. The comparison function should be used for all comparisons. If the list is empty, the function should return `None`.
"""

def advanced_median(l: list, cmp_func: callable):
    def select(lst, left, right, index):
        if left == right:
            return lst[left]

        pivot_index = get_pivot(lst, left, right)
        pivot_index = partition(lst, left, right, pivot_index, cmp_func)
        if index == pivot_index:
            return lst[pivot_index]
        elif index < pivot_index:
            return select(lst, left, pivot_index-1, index)
        else:
            return select(lst, pivot_index+1, right, index)

    def partition(lst, left, right, pivot_index, cmp_func):
        pivot_value = lst[pivot_index]
        lst[pivot_index], lst[right] = lst[right], lst[pivot_index]
        store_index = left
        for i in range(left, right):
            try:
                if cmp_func(lst[i], pivot_value) < 0:
                    lst[store_index], lst[i] = lst[i], lst[store_index]
                    store_index += 1
            except TypeError as te:
                print(f'Error: Mismatch of data types that cannot be compared {te}')
                return -1
        lst[right], lst[store_index] = lst[store_index], lst[right]
        return store_index

    def get_pivot(lst, left, right):
        mid = (right-left) // 2 + left
        return sorted([left, mid, right])[1]

    if l:
        if len(l) % 2 == 1:
            return select(l[:], 0, len(l)-1, len(l) // 2)
        else:
            left = select(l[:], 0, len(l)-1, len(l) // 2 - 1)
            right = select(l[:], 0, len(l)-1, len(l) // 2)
            try:
                return (left + right) / 2.0
            except TypeError as te:
                print(f'Error: Mismatch of data types that cannot be calculated {te}')
                return None
    return None