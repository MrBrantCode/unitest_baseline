"""
QUESTION:
Write a function `longestNonRepeatingSubstring` that takes a string `s` as input and returns the longest substring of consecutive, non-repeating characters within `s`. If there are multiple substrings with the same length, return the first one found. If there are no non-repeating substrings, return an empty string.
"""

def longestNonRepeatingSubstring(s: str) -> str:
    longest_substring = ""
    current_substring = ""
    seen_chars = set()
    start = 0

    for end in range(len(s)):
        if s[end] in seen_chars:
            while s[start] != s[end]:
                seen_chars.remove(s[start])
                start += 1
            start += 1
        else:
            seen_chars.add(s[end])
            current_substring = s[start:end+1]
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring

    return longest_substring