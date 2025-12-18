"""
QUESTION:
Write a function named `minWindow` that takes two strings `s` and `t` as input and returns the minimum window in `s` that contains all characters in `t`. The function should also return the minimum length of the window. 

The function should use the sliding window technique and return the minimum window string. The window should contain all unique characters in `t` and the length of the window should be minimum among all possible windows in `s`.
"""

def minWindow(s, t):
    left = 0
    right = 0
    countChar = 0
    countT = len(set(t))
    minWindowLen = float('inf')
    minWindowString = ""

    dictT = {}
    for char in t:
        dictT[char] = dictT.get(char, 0) + 1

    while right < len(s):
        if s[right] in dictT:
            dictT[s[right]] -= 1
            if dictT[s[right]] == 0:
                countChar += 1

        while countChar == countT:
            if right - left + 1 < minWindowLen:
                minWindowLen = right - left + 1
                minWindowString = s[left:right+1]

            if s[left] in dictT:
                dictT[s[left]] += 1
                if dictT[s[left]] > 0:
                    countChar -= 1

            left += 1

        right += 1

    return minWindowString