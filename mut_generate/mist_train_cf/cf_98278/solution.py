"""
QUESTION:
Write a function `find_string_with_most_vowels` that takes a list of strings as input and returns the string with the highest number of vowels, excluding strings with less than five characters and those containing numbers. If multiple strings have the same highest vowel count, return the first occurrence in the input list.
"""

def find_string_with_most_vowels(strings):
    vowels = set('aeiouAEIOU')
    max_vowels_count = -1
    max_vowels_string = None
    for string in strings:
        if len(string) < 5 or any(char.isdigit() for char in string):
            continue
        vowels_count = sum(1 for char in string if char in vowels)
        if vowels_count > max_vowels_count:
            max_vowels_count = vowels_count
            max_vowels_string = string
    return max_vowels_string