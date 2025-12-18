"""
QUESTION:
Create a function `detect_and_replace(k, strs, replacement)` that takes as input a positive integer `k`, a list of strings `strs`, and a replacement string `replacement`. The function should return a list of strings where all substrings of length `k` or more that appear more than once in the same string are removed, and substrings of length `k` or more that appear in different strings are replaced by the `replacement` string.
"""

def detect_and_replace(k, strs, replacement):
    # Count the occurences of each substring with length k
    counts = {}
    for s in strs:
        for i in range(len(s) - k + 1):
            sub = s[i:i+k]
            if sub not in counts:
                counts[sub] = 0
            counts[sub] += 1

    # Replace substrings that occur more than once
    result = []
    for s in strs:
        temp = s
        for sub, count in counts.items():
            if count > 1:
                temp = temp.replace(sub, replacement)
        result.append(temp)
    return result