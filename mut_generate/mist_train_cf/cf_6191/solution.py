"""
QUESTION:
Create a function called `longest_vowel_substring` that takes a string as input and returns the longest substring of consecutive characters that contains all vowels and occurs at least twice in the string. If multiple substrings have the same length and satisfy these conditions, return the one that occurs first.
"""

def longest_vowel_substring(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_length = 0
    longest_substring = ""

    for i in range(len(s)):
        if s[i] in vowels:
            for j in range(i+1, len(s)):
                if s[j] not in vowels:
                    break
                substring = s[i:j+1]
                if s.count(substring) >= 2 and len(substring) > max_length:
                    max_length = len(substring)
                    longest_substring = substring

    return longest_substring