"""
QUESTION:
Write a function `queryString(S, N)` that takes a binary string `S` and a positive integer `N` as input. The function should return a boolean value indicating whether the binary representation of every integer from 1 to `N` is a substring of `S` and the count of unique substrings of `S` that can be represented as binary numbers from 1 to `N`. The length of `S` is between 1 and 1000, and `N` is between 1 and 10^9.
"""

def queryString(S, N):
    count = 0
    for i in range(N, 0, -1):
        binary = bin(i)[2:]
        if binary in S:
            count += 1
        else:
            return False, count
    return True, count