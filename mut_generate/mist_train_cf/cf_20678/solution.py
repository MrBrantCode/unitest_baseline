"""
QUESTION:
Given two strings s and t, write a function `minWindow(s, t)` that returns the minimum window in s which will contain all the characters in t. The function should also return the minimum length of the window. Do not use any built-in functions or libraries to solve this problem.
"""

def minWindow(s, t):
    left, right = 0, 0
    count = 0
    minLen = float('inf')
    start = 0
    
    t_freq = {}
    for char in t:
        if char in t_freq:
            t_freq[char] += 1
        else:
            t_freq[char] = 1
    
    s_freq = {}
    
    while right < len(s):
        char = s[right]
        if char in s_freq:
            s_freq[char] += 1
        else:
            s_freq[char] = 1
            
        if char in t_freq and s_freq[char] <= t_freq[char]:
            count += 1
        
        if count == len(t):
            while s[left] not in t_freq or s_freq[s[left]] > t_freq[s[left]]:
                s_freq[s[left]] -= 1
                left += 1
            
            windowLen = right - left + 1
            if windowLen < minLen:
                minLen = windowLen
                start = left
        
        right += 1
    
    if minLen == float('inf'):
        return ""
    return s[start:start+minLen]