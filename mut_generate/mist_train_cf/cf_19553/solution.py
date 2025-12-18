"""
QUESTION:
Design an algorithm to find the longest substring with no repeating characters in a given string and return the substring along with its length. The input string may contain lowercase and uppercase letters, spaces, and special characters, and the substring is case-sensitive. If there are multiple longest substrings, return any one of them. Use a sliding window approach without any additional data structures.
"""

def entance(s):
    start = 0
    end = 0
    maxLen = 0
    maxLengthString = ""
    seen = set()

    while end < len(s):
        if s[end] not in seen:
            seen.add(s[end])
            if end - start + 1 > maxLen:
                maxLen = end - start + 1
                maxLengthString = s[start:end+1]
            end += 1
        else:
            seen.remove(s[start])
            start += 1

    return maxLengthString, maxLen