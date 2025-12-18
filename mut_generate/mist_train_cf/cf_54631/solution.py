"""
QUESTION:
Write a function `shortest_string_without_vowels` that takes three string inputs `str1`, `str2`, and `str3` and returns the shortest string among them after removing all vowels. Vowels are defined as 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'. If multiple strings have the same minimum length after removing vowels, any of them can be returned.
"""

def shortest_string_without_vowels(str1, str2, str3):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    str1_without_vowels = "".join([char for char in str1 if char not in vowels])
    str2_without_vowels = "".join([char for char in str2 if char not in vowels])
    str3_without_vowels = "".join([char for char in str3 if char not in vowels])
    
    return min(str1_without_vowels, str2_without_vowels, str3_without_vowels, key=len)