"""
QUESTION:
Given a string `s` of lowercase letters, find the intervals of every large group of consecutive characters, where a group is considered large if it has 3 or more characters. The function `largeGroupPositions(s)` should return the intervals of these large groups in increasing order by start index, along with the character that forms each large group. The function should take a string `s` as input, where `1 <= s.length <= 1000` and `s` contains only lowercase English letters.
"""

def largeGroupPositions(s):
    res = []
    i = 0 
    for j in range(len(s)):
        if j == len(s) - 1 or s[j] != s[j+1]:
            if j - i + 1 >= 3:
                res.append([i, j, s[i]])
            i = j + 1
    return res