"""
QUESTION:
Create a function `remove_duplicates_and_count` that takes a string `s` as input and returns a tuple containing the modified string with duplicates removed in the order of their first occurrence in the original string, and the count of distinct characters in the string. The function should ignore case sensitivity and consider spaces and punctuation as characters.
"""

def remove_duplicates_and_count(s):
    freq = {}
    res = ""
    for char in s:
        if char.lower() not in [key.lower() for key in freq]:
            freq[char] = 1
            res += char
        else:
            freq[char] = freq.get(char, 0) + 1
    return res, len(freq.keys())