"""
QUESTION:
Implement the `fib_search` function to find the index of a target element `x` in a sorted array `arr` using the Fibonacci search technique. The array `arr` is guaranteed to be in ascending order. Return the index of the target element if found, otherwise return -1. The function should take two parameters: `arr` (the sorted array) and `x` (the target element).
"""

def fib_search(arr, x):
    fib_2 = 0
    fib_1 = 1
    fib_m = fib_2 + fib_1

    while (fib_m < len(arr)):
        fib_2 = fib_1
        fib_1 = fib_m
        fib_m = fib_2 + fib_1

    index = -1

    while (fib_m > 1):
        i = min(index + fib_2 , (len(arr)-1))

        if (arr[i] < x):
            fib_m = fib_1
            fib_1 = fib_2
            fib_2 = fib_m - fib_1
            index = i
        elif (arr[i] > x):
            fib_m = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_m - fib_1
        else:
            return i

    if(fib_1 and index<(len(arr)-1) and arr[index+1] == x):
        return index+1

    return -1