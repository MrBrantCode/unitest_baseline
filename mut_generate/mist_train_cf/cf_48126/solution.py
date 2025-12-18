"""
QUESTION:
Implement a function `ternary_search` that takes four parameters: `l` (the starting index), `r` (the ending index), `key` (the value to be searched), and `ar` (a sorted array with distinct values). The function should return the index of the `key` in the array if found, and -1 otherwise.
"""

def ternary_search(l, r, key, ar):
    if (r >= l):
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3

        # If key is present at mid1
        if (ar[mid1] == key):
            return mid1

        # If key is present at mid2
        if (ar[mid2] == key):
            return mid2

        # If key not present and key smaller than mid1
        if (ar[mid1] > key):
            return ternary_search(l, mid1-1, key, ar)

        # If key not present and key greater than mid2
        elif (ar[mid2] < key):
            return ternary_search(mid2+1, r, key, ar)

        # If key present in mid1 to mid2
        else:
            return ternary_search(mid1+1, mid2-1, key, ar)

    # If key not found
    return -1