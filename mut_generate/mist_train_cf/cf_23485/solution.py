"""
QUESTION:
Rearrange the characters in a given string such that no two consecutive characters are the same. Implement a function `rearrange_string(s)` where `s` is the input string. The function should return the rearranged string. The input string only contains lowercase English letters.
"""

def rearrange_string(s):
    arr = list(s)
    i, j = 0, 1
    while i < len(arr):
        if i+1 < len(arr) and arr[i] == arr[i+1]:
            while j < len(arr):
                if arr[j] != arr[i]:
                    arr[i+1], arr[j] = arr[j], arr[i+1]
                    break
                j += 1
        i += 1
    return "".join(arr)