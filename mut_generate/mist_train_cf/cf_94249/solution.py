"""
QUESTION:
Write a function `longest_substring_with_vowel(s)` that takes a string `s` as input and returns the length of the longest substring without repetition that contains at least one vowel. The vowels are defined as 'a', 'e', 'i', 'o', and 'u'.
"""

def longest_substring_with_vowel(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    start = 0
    end = 0
    unique_chars = set()
    max_length = 0
    max_vowel_length = 0

    while end < len(s):
        if s[end] not in unique_chars:
            unique_chars.add(s[end])
            end += 1
        else:
            current_length = end - start
            if current_length > max_length:
                if any(char in vowels for char in s[start:end]):
                    max_vowel_length = current_length
                max_length = current_length

            unique_chars.remove(s[start])
            start += 1

    return max_vowel_length