"""
QUESTION:
Implement a function `manacher` that takes a string `s` as input and returns the longest palindromic substring in `s`. The function should have a time complexity of O(n), where n is the length of `s`, and should be able to handle strings of up to 10^6 characters.
"""

def manacher(s):
    # Preprocess the input string to add special characters '#' between each pair of characters
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0

    for i in range(1, n-1):
        P[i] = (R > i) and min(R - i, P[2*C - i]) 
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > R:
            C, R = i, i + P[i]

    # Find the maximum element in P.
    maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
    return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]