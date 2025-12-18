"""
QUESTION:
Construct a function `longest_nice_substring(s)` that takes a string `s` as input and returns the lengthiest 'pleasant' substring. A substring is 'pleasant' if it includes every alphabet character it contains in both uppercase and lowercase variants. If multiple 'pleasant' substrings of identical length exist, return the one that occurs first. If no 'pleasant' substrings are found, return an empty string. The length of `s` ranges from 1 to 100, inclusive, and `s` is composed of uppercase and lowercase English alphabets.
"""

def longest_nice_substring(s):
    max_length = 0
    result = ""
    for i in range(len(s)):
        upper = set()
        lower = set()
        for j in range(i, len(s)):
            if s[j].isupper():
                upper.add(s[j])
            else:
                lower.add(s[j].upper())
            if len(upper - lower) == 0 and len(lower - upper) == 0 and j - i + 1 > max_length:
                max_length = j - i + 1
                result = s[i: j + 1]
    return result