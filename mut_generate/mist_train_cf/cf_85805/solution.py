"""
QUESTION:
The function `rearrange_two_operations(arr, bit_shift_allowed=True)` takes an array of integers and a boolean indicating whether a bit-level shift operation is allowed. The goal is to determine if it's feasible to obtain a sorted, non-decreasing array within two operations: at most one swap of two elements and at most one bit-level shift operation on one element. The final array should contain an even number of elements that are strictly less than the first element in the original array sequence. The function should return True if it's feasible to obtain the sorted array and False if it's not. For an empty array, the function should also return True.
"""

def rearrange_two_operations(arr, bit_shift_allowed=True):
    """
    Given an array 'arr' comprising N integers arr[1], arr[2], ..., arr[N]. The integers within the array
    are randomly ordered. The goal is to determine if it's feasible to obtain a sorted, non-decreasing array by
    following these steps:
        1. Use a swap operation to exchange exactly a pair of elements in the array.
        2. If permitted and needed, execute a bit-level shift operation on exactly one element.
         - A right shift operation (x >> y) divides x by 2^y
         - A left shift operation (x << y) multiplies x by 2^y
        3. The total number of performed operations(minimal swaps and maximal bit-level shifts) must not exceed two.

    The function should return True if it's feasible to obtain the sorted array and False if it's not.
    For an empty array, the function should also return True.

    Note: The list can contain distinct or identical elements. The bit-level shift operation is optional 
    and can be turned off by setting the 'bit_shift_allowed' parameter to 'False'.

    """
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    if len(arr) == 0 or is_sorted(arr):
        return True

    first_element = arr[0]
    less_than_first = sum(1 for x in arr if x < first_element)

    if less_than_first % 2 != 0:
        return False

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            swapped_arr = arr[:i] + [arr[j]] + arr[i + 1:j] + [arr[i]] + arr[j + 1:]
            if is_sorted(swapped_arr):
                return True

            if bit_shift_allowed:
                for k in range(len(swapped_arr)):
                    for shift in range(1, 32):  
                        shifted_arr = swapped_arr[:k] + [swapped_arr[k] >> shift] + swapped_arr[k + 1:]
                        if is_sorted(shifted_arr):
                            return True
                        shifted_arr = swapped_arr[:k] + [swapped_arr[k] << shift] + swapped_arr[k + 1:]
                        if is_sorted(shifted_arr):
                            return True

    return False