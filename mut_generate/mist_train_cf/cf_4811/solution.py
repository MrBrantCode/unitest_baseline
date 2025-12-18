"""
QUESTION:
Write a function `find_longest_substring(s)` that finds the longest substring with no repeating characters in a given string `s`. The function should return the longest substring and its length should be as long as possible. 

The input string `s` may contain both lowercase and uppercase letters, spaces, and special characters. The substring is case-sensitive, meaning "a" and "A" are considered different characters. If there are multiple longest substrings with no repeating characters, return any one of them.

The algorithm should have a time complexity of O(n), where n is the length of the string `s`. You are allowed to use a set data structure to keep track of the characters in the current substring.
"""

def find_longest_substring(s):
    start = 0
    maxLength = 0
    maxStart = 0
    maxEnd = 0
    charSet = set()

    for end in range(len(s)):
        while s[end] in charSet:
            charSet.remove(s[start])
            start += 1
        charSet.add(s[end])
        if end - start + 1 > maxLength:
            maxLength = end - start + 1
            maxStart = start
            maxEnd = end

    return s[maxStart:maxEnd+1]