"""
QUESTION:
Write a function called `superior_vowel_compilation` that takes a string `s` as input, calculates the total number of vowels (both lowercase and uppercase) present in the string, and considers 'y' as a vowel only if it's at the end of the string. The function should be case-insensitive and work with non-English characters. Additionally, write test cases to verify the correctness of the function for standard letters, uppercase letters, and special characters.
"""

def superior_vowel_compilation(s):
    vowels = 'aeiou'
    s = s.lower()
    count = sum(1 for c in s if c in vowels)
    if s and s[-1] == 'y':
        count += 1
    return count