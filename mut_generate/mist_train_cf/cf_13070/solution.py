"""
QUESTION:
Write a function `minWindow(s, t)` that finds the minimum window in string `s` which will contain all the characters in string `t`. The function should return the minimum window string. If no such window exists, return an empty string. The function should assume that all characters in `s` and `t` are lowercase letters and that `s` and `t` are non-empty strings.
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