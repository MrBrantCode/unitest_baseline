"""
QUESTION:
Write a function `longest_unique_substring` that takes a string as input and returns the longest substring of the given string that contains only unique characters. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(k), where k is the length of the longest substring without repeating characters.
"""

def longest_unique_substring(string):
    longestSubstring = ""
    charMap = {}
    start = 0
    end = 0

    while end < len(string):
        if string[end] in charMap:
            start = max(start, charMap[string[end]] + 1)
        charMap[string[end]] = end
        substring = string[start:end+1]
        if len(substring) > len(longestSubstring):
            longestSubstring = substring
        end += 1

    return longestSubstring