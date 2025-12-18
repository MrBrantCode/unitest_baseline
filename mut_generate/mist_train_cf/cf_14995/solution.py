"""
QUESTION:
Write a function `sort_strings_by_vowels` that takes two strings as input and returns them in order of the number of vowels present in each string. If both strings have the same number of vowels, they should be sorted in alphabetical ascending order. The function should not modify the original strings.
"""

def sort_strings_by_vowels(str1, str2):
    vowels = 'aeiou'
    def count_vowels(s):
        return sum(1 for char in s.lower() if char in vowels)

    if count_vowels(str1) < count_vowels(str2):
        return str1, str2
    elif count_vowels(str1) > count_vowels(str2):
        return str2, str1
    else:
        return min(str1, str2), max(str1, str2)