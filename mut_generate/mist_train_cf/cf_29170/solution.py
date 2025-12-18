"""
QUESTION:
Implement a function `rearrange_string(S: str) -> str` that takes a string `S` as input, rearranges it such that all the non-alphabetic characters are moved to the end of the string while maintaining the relative order of the alphabetic characters, and returns the modified string. The input string `S` has a length between 1 and 10^5, inclusive, and contains alphanumeric and non-alphanumeric characters.
"""

def rearrange_string(S: str) -> str:
    arr = list(S)
    i, j = 0, len(arr) - 1
    while i < j:
        if not arr[i].isalpha():
            i += 1
        elif not arr[j].isalpha():
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return ''.join(arr)