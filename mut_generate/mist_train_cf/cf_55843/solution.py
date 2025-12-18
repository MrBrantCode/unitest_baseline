"""
QUESTION:
Write a function `prevPermOpt1` that takes an array of positive integers `arr` as input, and returns the lexicographically largest permutation that is smaller than `arr`, which can be made with exactly one swap of two elements that are not the first or last element of the array. If no such permutation exists, return the original array.

The input array `arr` has the following constraints: `3 <= len(arr) <= 10^4` and `1 <= arr[i] <= 10^4`. The swap operation cannot involve the first or last element of the array.
"""

def prevPermOpt1(arr):
    N = len(arr)
    left = N - 2

    while left >= 1 and arr[left] <= arr[left + 1]:
        left -= 1
    
    if left == 0:
        return arr

    right = left + 1
    while right + 1 < N and arr[right + 1] < arr[left]:
        if arr[right + 1] == arr[right]:
            right += 1
        else:
            break

    arr[left], arr[right] = arr[right], arr[left]
    return arr