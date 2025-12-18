"""
QUESTION:
Given a string s consisting of characters 'D' and 'I', representing decreasing and increasing relationships respectively, find the lexicographically smallest and largest permutations of the array [1, 2, ..., n] that can represent the given secret signature, where n is the length of s plus 1.

Implement a function findPermutation(s) that returns the two permutations as lists. The input string s will only contain the characters 'D' and 'I' and its length is a positive integer not exceeding 10,000.
"""

def findPermutation(s):
    l = r = 1
    n = len(s)
    min_arr = [0] * (n + 1)
    max_arr = [0] * (n + 1)
    for i in range(n):
        if s[i] == 'I':
            min_arr[i] = l
            max_arr[i] = r
            l += 1
            r += 1
        else:
            min_arr[i] = r
            max_arr[i] = l
            r -= 1
            l -= 1
    min_arr[-1] = l
    max_arr[-1] = r
    return min_arr, max_arr