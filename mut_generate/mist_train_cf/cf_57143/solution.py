"""
QUESTION:
Write a function `swap_arr_values(arr1, arr2)` that swaps the values of two arrays `arr1` and `arr2` without using temporary variables. The function should handle arrays of unequal lengths, where the maximum length of the arrays can be up to 10^6 elements. Assume that `arr1` initially contains elements set to 10 and `arr2` initially contains elements set to 20. The function should return the swapped arrays.
"""

def swap_arr_values(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    for i in range(min(n, m)):
        arr1[i] = arr1[i] + arr2[i] 
        arr2[i] = arr1[i] - arr2[i] 
        arr1[i] = arr1[i] - arr2[i] 

    if n > m:
        for i in range(m, n):
            arr1[i] = 20
    elif m > n:
        for i in range(n, m):
            arr2[i] = 10

    return arr1, arr2