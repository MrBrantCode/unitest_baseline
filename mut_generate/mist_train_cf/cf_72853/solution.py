"""
QUESTION:
Develop a function named `quantify_chars` that takes a string `s` as input and returns a dictionary containing the count of characters that are flanked by vowels on either side in the string. Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both lowercase and uppercase), and the function should be case sensitive.
"""

def quantify_chars(s):
    vowels = "aeiouAEIOU"

    counts = {}

    for i in range(1, len(s) - 1):    # Start from 1 and end at len(s) - 1 to avoid out-of-range errors
        if s[i-1] in vowels and s[i+1] in vowels:
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1

    return counts