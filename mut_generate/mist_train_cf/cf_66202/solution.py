"""
QUESTION:
Create a function `ternary_search` that performs a ternary search on a single-dimensional sorted array. The function should recognize whether the array is sorted in ascending or descending order and perform the appropriate ternary search. The function should take in four parameters: `l` (the left index of the array), `r` (the right index of the array), `key` (the target value to search for), and `ar` (the sorted array). The function should return the index of the `key` if found, and -1 otherwise.
"""

def ternary_search(l, r, key, ar):
    if not ar:
        return -1  # Edge case of empty array
    if len(ar) == 1:
        return 0 if ar[0] == key else -1
    if r < l:
        return -1
    if ar[0] < ar[-1]:  # Array is sorted in ascending order
        if key < ar[l]:
            return -1
        if key > ar[r]:
            return -1
    else:  # Array is sorted in descending order
        if key > ar[l]:
            return -1
        if key < ar[r]:
            return -1
    mid1 = l + (r - l) // 3
    mid2 = r - (r - l) // 3
    if ar[mid1] == key:
        return mid1
    elif ar[mid2] == key:
        return mid2
    elif (ar[0] < ar[-1] and key < ar[mid1]) or (ar[0] > ar[-1] and key > ar[mid1]):
        return ternary_search(l, mid1 - 1, key, ar)
    elif (ar[0] < ar[-1] and key > ar[mid2]) or (ar[0] > ar[-1] and key < ar[mid2]):
        return ternary_search(mid2 + 1, r, key, ar)
    else:
        return ternary_search(mid1 + 1, mid2 - 1, key, ar)