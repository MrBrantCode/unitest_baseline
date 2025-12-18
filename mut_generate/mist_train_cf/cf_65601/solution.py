"""
QUESTION:
You are given two strings `s` and `t` of the same length, and an integer `maxCost`. The goal is to change `s` to `t` by changing characters with costs equal to the absolute difference of their ASCII values. You need to find the maximum length of a substring of `s` that can be changed to be the same as the corresponding substring of `t` with a cost less than or equal to `maxCost`. If there are multiple substrings with the same maximum length, return the starting index of the first such substring.

Write a function `equalSubstring` that takes `s`, `t`, and `maxCost` as input and returns a list of two integers where the first one is the starting index of the maximum length substring and the second one is the maximum length. 

Constraints: `1 <= s.length, t.length <= 10^5`, `0 <= maxCost <= 10^6`, and `s` and `t` only contain lower case English letters.
"""

def equalSubstring(s: str, t: str, maxCost: int) -> [int, int]:
    left = 0 # left pointer of the sliding window
    max_len = 0 # maximum length of the substring
    costs = [0] * len(s) # cost of changing every character in s to corresponding character in t

    # calculate the cost for every character
    for i in range(len(s)):
        costs[i] = abs(ord(s[i]) - ord(t[i]))

    # sliding window
    for right in range(len(s)):
        maxCost -= costs[right] # subtract the cost from maxCost
        if maxCost < 0: # if maxCost is less than 0
            maxCost += costs[left] # add the cost of the character at the left pointer
            left += 1 # move the left pointer forward
        # calculate the maximum length
        max_len = max(max_len, right - left + 1)
        
    return [left, max_len]