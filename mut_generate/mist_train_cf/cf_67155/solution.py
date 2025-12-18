"""
QUESTION:
Write a function `shortest_excluding_vowels` that takes three distinct strings as parameters and returns the shortest string that strictly excludes any presence of vowel characters (both lowercase and uppercase), numbers, and special characters. The function should handle strings that may contain non-alphanumeric characters and have a time complexity of O(n), where n is the total number of characters in all three strings.
"""

def shortest_excluding_vowels(str1, str2, str3):
    vowel_chars = list('aeiouAEIOU0123456789!@#$%^&*()_+=-[]{}|;:,.<>?/`~"')
    filtered_strings = [''.join(ch for ch in string if ch not in vowel_chars) for string in [str1, str2, str3]]
    return min(filtered_strings, key=len)