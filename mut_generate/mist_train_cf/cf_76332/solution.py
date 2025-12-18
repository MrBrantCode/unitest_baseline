"""
QUESTION:
Write a function `longest_common_substring(arr)` that takes an array of unique strings as input and returns the longest common consecutive alphabetic substring shared uniformly among every individual string within the array's confines. The function should assume that "consecutively" means the alphabets should be present in the same order in all strings, and it is case-sensitive.
"""

def longest_common_substring(arr):
    arr.sort()  # sorted list
    n = min(arr, key=len)  # smallest string
    i = 0
    while i < len(n):  
        for string in arr[1:]:
            if i >= len(string) or n[i] != string[i]:  
                return n[:i]
        i += 1

    return n  # return the common prefix substring