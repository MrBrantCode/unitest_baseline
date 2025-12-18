"""
QUESTION:
Given a unique integer array `arr` and another array of integer arrays `pieces`, where integers in `pieces` are unique, determine if `arr` can be constructed by concatenating the arrays in `pieces` in any sequence without reordering the integers in each individual array `pieces[i]`. The function should return `true` if `arr` can be constructed from `pieces`, otherwise return `false`.

The function should be named `canFormArray` and take two parameters: `arr` and `pieces`. The constraints are:
- 1 <= pieces.length <= arr.length <= 100
- sum(pieces[i].length) == arr.length
- 1 <= pieces[i].length <= arr.length
- 1 <= arr[i], pieces[i][j] <= 100
"""

def canFormArray(arr, pieces):
    pieces_dict = {p[0]: p for p in pieces}
    i = 0
    while i < len(arr):
        if arr[i] in pieces_dict:
            p = pieces_dict[arr[i]]
            if arr[i:i+len(p)] != p:
                return False
            i += len(p)
        else:
            return False
    return True