"""
QUESTION:
Write a function `canFormArray` that determines if it is possible to assemble a given array `arr` by concatenating arrays from a list of arrays `pieces`. Each array in `pieces` must be used exactly once and its elements must not be rearranged. The function should return `true` if `arr` can be assembled, and `false` otherwise.

The function must work with the following constraints:

- `1 <= len(pieces) <= len(arr) <= 100`
- The total length of all arrays in `pieces` is equal to the length of `arr`.
- `1 <= len(piece) <= len(arr)`
- `1 <= arr[i], pieces[i][j] <= 100`
- All integers in `arr` and `pieces` are distinct.
"""

def canFormArray(arr, pieces):
    index = {x: i for i, x in enumerate(arr)}
    for piece in pieces:
        if len(piece) == 1:
            if piece[0] not in index:
                return False
        else:
            for i in range(len(piece) - 1):
                if piece[i+1] not in index or index[piece[i]] + 1 != index[piece[i+1]]:
                    return False
    return True