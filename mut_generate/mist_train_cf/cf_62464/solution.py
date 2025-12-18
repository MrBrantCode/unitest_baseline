"""
QUESTION:
Given an array of unique strings `words` containing only lowercase English letters, implement a function `string_matching(words)` that returns a list of tuples, where each tuple contains a substring and its count. A substring is defined as a string that can be obtained by removing characters from the left and/or right side of another string. The function should only include substrings that appear in at least one other string in the array. The input array has a length between 1 and 100, and each string has a length between 1 and 30.
"""

def string_matching(words):
    words.sort(key = len) 
    substrings = {}
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] in words[j]: 
                if words[i] in substrings: 
                    substrings[words[i]] += 1
                else: 
                    substrings[words[i]] = 1
    return list(substrings.items())