"""
QUESTION:
Design a function called `substring` that takes a string `s` as input and returns the longest subsequence with non-repeating and non-consecutive characters. The result should maintain the order of characters as they appear in the input string.
"""

def substring(s):
    start = 0
    used_chars = {}
    max_substring = ""

    for i, char in enumerate(s):
        if char in used_chars and used_chars[char] >= start:
            start = used_chars[char] + 1
        else:
            if len(s[start:i+1]) > len(max_substring):
                max_substring = s[start:i+1]

        used_chars[char] = i

    return max_substring