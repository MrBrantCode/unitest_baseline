"""
QUESTION:
Write a function called `find_longest_substring_with_vowel_and_digit` that takes a string `s` as input and returns the length of the longest substring without repetition that contains at least one vowel and one digit. The function should iterate through the string using a sliding window technique and keep track of the maximum length of the substring without repetition and the maximum length of the substring with at least one vowel and one digit.
"""

def find_longest_substring_with_vowel_and_digit(s):
    vowels = set("aeiouAEIOU")
    digits = set("0123456789")

    start = 0
    end = 0
    unique_chars = set()
    max_length = 0
    max_vowel_digit_length = 0

    while end < len(s):
        char = s[end]
        if char not in unique_chars:
            unique_chars.add(char)
            end += 1
            length = end - start
            if length > max_length:
                max_length = length
                if any(char in vowels for char in unique_chars) and any(char in digits for char in unique_chars):
                    max_vowel_digit_length = max_length
        else:
            unique_chars.remove(s[start])
            start += 1

    return max_vowel_digit_length