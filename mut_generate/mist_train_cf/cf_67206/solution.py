"""
QUESTION:
Write a function `count_substrings(s)` that takes a string `s` as input and returns a dictionary where the keys are the substrings with only one distinct letter and the values are their respective frequencies. The string `s` consists of only lowercase English letters and has a length between 1 and 1000.
"""

def count_substrings(s):
    result = {}
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        for k in range(i, j):
            for l in range(k, j):
                substring = s[k: l+1]
                if substring in result:
                    result[substring] += 1
                else:
                    result[substring] = 1
        i = j
    return result