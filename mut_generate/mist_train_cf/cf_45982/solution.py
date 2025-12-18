"""
QUESTION:
Create a function called `find_vowels` that takes a string `s` as input. The function should return a list of tuples, where each tuple contains a vowel character and its index in the string. The function should ignore consecutive occurrences of the same vowel, only including the first occurrence of consecutive vowels. Vowels are defined as 'a', 'e', 'i', 'o', and 'u', and the function should be case-insensitive.
"""

def find_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    i = 0
    while i < len(s):
        if s[i].lower() in vowels:
            output.append((s[i], i))
            count = 1
            while i + count < len(s) and s[i + count].lower() == s[i].lower():
                count += 1
            if count > 1:
                i += count - 1
        i += 1
    return output